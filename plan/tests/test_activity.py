from faker import Faker
from django.test import TestCase
from model_bakery import baker

from virtuagym.common.test_tools import ListCreateBaseTestCase
from plan.models import Activity
from plan.serializers.activity_serializer import ActivityReadSerializer, ActivityWriteSerializer
from plan.urls import ACTIVITY


class ActivitiesListCreateAPITest(ListCreateBaseTestCase, TestCase):
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
    model_class = Activity
    read_serializer_class = ActivityReadSerializer
    write_serializer_class = ActivityWriteSerializer
    url_name = ACTIVITY
    quantity = 15

    name = Faker().name()
    model_testing_field = 'name'
    model_testing_field_value = name
    valid_data = {'name': name, 'workout': 1}
    invalid_data = {'invalid': 'ha'}

    def setUp(self):
        super().setUp()
        baker.make('plan.Workout')
