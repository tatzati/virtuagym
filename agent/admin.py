from django.contrib import admin
from agent.models import User


# Register your models here.
class MyUser(admin.ModelAdmin):
    list_display = ('email', 'name')  # fields to display in the listing
    empty_value_display = '-empty-'  # display value when empty
    list_filter = ('email',)  # enable results filtering
    list_per_page = 25  # number of items per page
    ordering = ['email']  # Default results ordering


admin.site.register(User, MyUser)
