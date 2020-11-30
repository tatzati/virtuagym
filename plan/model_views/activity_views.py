from virtuagym.common.helper import CommonListCreateAPIView, CommonRetrieveUpdateDestroyAPIView
from plan.models import Activity
from plan.serializers.activity_serializer import ActivityReadSerializer, ActivityWriteSerializer


class ActivityListCreateAPIView(CommonListCreateAPIView):
    """
    get:
    Return a list of activity instances.

    post:
    Create a activity instance.
    """
    queryset = Activity.objects.filter(deleted=False)
    read_serializer_class = ActivityReadSerializer
    write_serializer_class = ActivityWriteSerializer
    internal_name = 'activity'


class ActivityRetrieveUpdateDestroyAPIView(CommonRetrieveUpdateDestroyAPIView):
    """
    get:
    Return a activity instance.

    put:
    Update a activity instance.

    delete:
    Delete a activity instance.

    patch:
    Update a activity instance partially.
    """
    queryset = Activity.objects.filter(deleted=False)
    read_serializer_class = ActivityReadSerializer
    write_serializer_class = ActivityWriteSerializer
    internal_name = 'activity'
