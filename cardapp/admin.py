from django.contrib import admin
from .models import User
# Register your models here.
@admin.register(User)
class User_register(admin.ModelAdmin):
    list_display=('name','email','password')