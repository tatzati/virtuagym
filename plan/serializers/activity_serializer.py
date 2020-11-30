from rest_framework.serializers import ModelSerializer

from plan.models import Activity
from plan.serializers.workout_serializer import WorkoutActivityReadSerializer


class ActivityReadSerializer(ModelSerializer):
    workout = WorkoutActivityReadSerializer()

    class Meta:
        model = Activity
        fields = ['id', 'name', 'workout']
        extra_kwargs = {'id': {'read_only': True}}


class ActivityWriteSerializer(ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'name', 'workout']
        extra_kwargs = {'id': {'read_only': True}, 'name': {'required': True}}
