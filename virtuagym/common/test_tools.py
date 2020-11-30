from django.db import IntegrityError
from django.urls import reverse
from model_bakery import baker
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from agent.models import User
from virtuagym.common import constants


# noinspection PyAttributeOutsideInit,PyUnresolvedReferences
class ListCreateBaseTestCase:
    app_label = None
    model_class = None
    read_serializer_class = None
    write_serializer_class = None
    quantity = 1
    url_name = None
    valid_data = None
    invalid_data = None
    model_testing_field = None
    model_testing_field_value = None
    url = None

    def setUp(self):
        self.valid_data = self.valid_data
        self.invalid_data = self.invalid_data
        self.url = reverse(self.url_name)
        self.client = generate_random_client_with_token()
        self.second_user = generate_user(email='a@admin.com', password='Test2020!')

    def test_obj_list(self):
        """
        Test that a GET api call:
        1. returns a list with the appropriate data
        2. returns a 200 OK status code.
        :return:
        """
        baker.make(self.app_label + f'.{self.model_class.__qualname__}', _quantity=self.quantity)
        response = self.client.get(self.url, format=constants.JSON_FORMAT)
        obj = self.model_class.objects.filter(deleted=False)
        serializer = self.read_serializer_class(obj, many=True)
        self.assertEqual(response.data[constants.DATA], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_obj_create(self):
        """
        Test that a POST api call:
        1. creates the object
        2. does so with the correct expected data fields
        3. returns a 201 CREATED status code
        """
        response = self.client.post(self.url, self.valid_data, format=constants.JSON_FORMAT)
        self.assertEqual(
            getattr(self.model_class.objects.first(), self.model_testing_field),
            self.model_testing_field_value
        )
        self.assertEqual(self.model_class.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class RetrieveUpdateDestroyBase:
    def test_obj_retrieve(self):
        pass

    def test_obj_update(self):
        pass

    def test_obj_delete(self):
        pass

    class Meta:
        abstract = True


def generate_user(email, password):
    user = User.objects.create_user(email=email, password=password)
    return user


def generate_user_with_token(email, password, user=None):
    client = APIClient()
    user = user if user else generate_user(email, password)
    token = TokenObtainPairSerializer.get_token(user)
    client.credentials(HTTP_AUTHORIZATION='Bearer {}'.format(token.access_token))
    return client


def generate_random_client_with_token():
    client = APIClient()
    try:
        user = User.objects.create_user(email=constants.TEST_USER_EMAIL, password=constants.TEST_USER_PASSWORD)
    except IntegrityError:
        user = User.objects.get(email=constants.TEST_USER_EMAIL)
    token = TokenObtainPairSerializer.get_token(user)
    client.credentials(HTTP_AUTHORIZATION='Bearer {}'.format(token.access_token))
    return client
