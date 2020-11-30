from django.urls import path

from plan.model_views.plan_views import PlanListCreateAPIView, PlanRetrieveUpdateDestroyAPIView
from plan.model_views.workout_views import WorkoutListCreateAPIView, WorkoutRetrieveUpdateDestroyAPIView
from plan.model_views.activity_views import ActivityListCreateAPIView, ActivityRetrieveUpdateDestroyAPIView

PLAN = 'plan'
WORKOUT = 'workout'
ACTIVITY = 'activity'

urlpatterns = [
    path('plan/', PlanListCreateAPIView.as_view(), name=PLAN),
    path('plan/<int:pk>/', PlanRetrieveUpdateDestroyAPIView.as_view(), name=PLAN),

    path('workout/', WorkoutListCreateAPIView.as_view(), name=WORKOUT),
    path('workout/<int:pk>/', WorkoutRetrieveUpdateDestroyAPIView.as_view(), name=WORKOUT),

    path('activity/', ActivityListCreateAPIView.as_view(), name=ACTIVITY),
    path('activity/<int:pk>/', ActivityRetrieveUpdateDestroyAPIView.as_view(), name=ACTIVITY),
]
