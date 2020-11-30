from django.contrib.auth import get_user_model
from faker import Faker
from django.test import TestCase

from virtuagym.common.test_tools import ListCreateBaseTestCase
from plan.models import Plan
from plan.serializers.plan_serializer import PlanReadSerializer, PlanWriteSerializer
from plan.urls import PLAN


class PlansListCreateAPITest(ListCreateBaseTestCase, TestCase):
    """
    Testing all api methods
    @app_label: a string that defines the app label
    @model_class: the actual model class like app.models.Model
    @read_serializer_class: the actual read serializer class like app.serializers.ModelReadSerializer
    @write_serializer_class: the actual write serializer class like app.serializers.ModelWriteSerializer
    @url_name: a string as defined in the urls.py file
    @model_testing_field: a string containing one of the models field
    @model_testing_field_value: a value for the testing field
    @valid_data: a dictionary that will serve as the post payload with valid data
    @invalid_data: a dictionary that will serve as the post payload with invalid data
    """
    app_label = 'plan'
    model_class = Plan
    read_serializer_class = PlanReadSerializer
    write_serializer_class = PlanWriteSerializer
    url_name = PLAN
    quantity = 15

    name = Faker().name()
    model_testing_field = 'name'
    model_testing_field_value = name
    valid_data = {'name': name, 'users': []}
    invalid_data = {'invalid': 'ha'}
