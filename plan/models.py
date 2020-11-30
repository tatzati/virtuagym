from django.db import models
from django.db.models.query import QuerySet


class PlanModel(models.Model):
    class Meta:
        app_label = 'plan'
        abstract = True

    deleted = models.BooleanField(default=False)


class PlanManager(QuerySet):

    def get_all(self):
        """Returns objects that are not deleted."""
        return self.filter(deleted=False)


class Plan(PlanModel):
    class Meta:
        db_table = 'plan'
        verbose_name = 'Plan'
        verbose_name_plural = 'Plans'

    """A Plan has a name and groups several ​Workout​ items."""
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Workout(PlanModel):
    class Meta:
        db_table = 'workout'
        verbose_name = 'Workout'
        verbose_name_plural = 'Workouts'

    """A ​Workout​ can have multiple ​Activity​ items that your a ​User​ will perform that day."""
    name = models.CharField(max_length=255, blank=True, null=True)
    plan = models.ForeignKey(Plan, related_name='workouts', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Activity(PlanModel):
    class Meta:
        db_table = 'activity'
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'

    """​Activity​ items that your ​User​ will perform that day."""
    name = models.CharField(max_length=255, blank=True, null=True)
    workout = models.ForeignKey(Workout, related_name='activities', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
