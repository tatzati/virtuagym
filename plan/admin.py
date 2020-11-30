from django.contrib import admin
from plan.models import Plan, Workout, Activity


# Register your models here.
class Custom(admin.ModelAdmin):
    list_display = ('name',)  # fields to display in the listing
    empty_value_display = '-empty-'  # display value when empty
    list_filter = ('name',)  # enable results filtering
    list_per_page = 25  # number of items per page
    ordering = ['name']  # Default results ordering


admin.site.register(Plan, Custom)
admin.site.register(Workout, Custom)
admin.site.register(Activity, Custom)
