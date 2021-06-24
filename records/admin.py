from django.contrib import admin
from .models import UserRegistration
# Register your models here.
@admin.register(UserRegistration)
class Useradmin(admin.ModelAdmin):
    list_display=['name','email','password','country']