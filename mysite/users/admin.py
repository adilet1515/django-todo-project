from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyCustomUser


@admin.register(MyCustomUser)
class MyCustomUserAdmin(UserAdmin):
    pass