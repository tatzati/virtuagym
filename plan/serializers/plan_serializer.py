from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer

from plan.models import Plan


class PlanReadSerializer(ModelSerializer):
    workouts = StringRelatedField(many=True)
    users = StringRelatedField(many=True)

    class Meta:
        model = Plan
        fields = ['id', 'name', 'workouts', 'users']
        extra_kwargs = {'id': {'read_only': True}}


class PlanWorkoutReadSerializer(ModelSerializer):
    users = StringRelatedField(many=True)

    class Meta:
        model = Plan
        fields = ['id', 'name', 'users']
        extra_kwargs = {'id': {'read_only': True}}


class PlanWriteSerializer(ModelSerializer):
    class Meta:
        model = Plan
        fields = ['id', 'name', 'users']
        extra_kwargs = {'id': {'read_only': True}, 'name': {'required': True}, 'users': {'required': False}}
