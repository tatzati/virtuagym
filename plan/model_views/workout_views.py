from virtuagym.common.helper import CommonListCreateAPIView, CommonRetrieveUpdateDestroyAPIView
from plan.models import Workout
from plan.serializers.workout_serializer import WorkoutReadSerializer, WorkoutWriteSerializer


class WorkoutListCreateAPIView(CommonListCreateAPIView):
    """
    get:
    Return a list of workout instances.

    post:
    Create a workout instance.
    """
    queryset = Workout.objects.filter(deleted=False)
    read_serializer_class = WorkoutReadSerializer
    write_serializer_class = WorkoutWriteSerializer
    internal_name = 'workout'


class WorkoutRetrieveUpdateDestroyAPIView(CommonRetrieveUpdateDestroyAPIView):
    """
    get:
    Return a workout instance.

    put:
    Update a workout instance.

    delete:
    Delete a workout instance.

    patch:
    Update a workout instance partially.
    """
    queryset = Workout.objects.filter(deleted=False)
    read_serializer_class = WorkoutReadSerializer
    write_serializer_class = WorkoutWriteSerializer
    internal_name = 'workout'
