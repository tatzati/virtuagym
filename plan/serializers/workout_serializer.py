from rest_framework.serializers import ModelSerializer

from plan.models import Workout
from plan.serializers.plan_serializer import PlanWorkoutReadSerializer


class WorkoutReadSerializer(ModelSerializer):
    plan = PlanWorkoutReadSerializer()

    class Meta:
        model = Workout
        fields = ['id', 'name', 'plan', 'activities']
        extra_kwargs = {'id': {'read_only': True}}


class WorkoutActivityReadSerializer(ModelSerializer):
    plan = PlanWorkoutReadSerializer()

    class Meta:
        model = Workout
        fields = ['id', 'name', 'plan']
        extra_kwargs = {'id': {'read_only': True}}


class WorkoutWriteSerializer(ModelSerializer):
    class Meta:
        model = Workout
        fields = ['id', 'name', 'plan']
        extra_kwargs = {'id': {'read_only': True}, 'name': {'required': True}, 'users': {'required': False}}
