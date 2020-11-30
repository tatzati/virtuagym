from virtuagym.common.helper import CommonListCreateAPIView, CommonRetrieveUpdateDestroyAPIView
from plan.models import Plan
from plan.serializers.plan_serializer import PlanReadSerializer, PlanWriteSerializer


class PlanListCreateAPIView(CommonListCreateAPIView):
    """
    get:
    Return a list of plan instances.

    post:
    Create a plan instance.
    """
    queryset = Plan.objects.filter(deleted=False)
    read_serializer_class = PlanReadSerializer
    write_serializer_class = PlanWriteSerializer
    internal_name = 'plan'


class PlanRetrieveUpdateDestroyAPIView(CommonRetrieveUpdateDestroyAPIView):
    """
    get:
    Return a plan instance.

    put:
    Update a plan instance.

    delete:
    Delete a plan instance.

    patch:
    Update a plan instance partially.
    """
    queryset = Plan.objects.filter(deleted=False)
    read_serializer_class = PlanReadSerializer
    write_serializer_class = PlanWriteSerializer
    internal_name = 'plan'
