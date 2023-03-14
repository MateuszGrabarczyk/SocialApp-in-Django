from .models import Profile
from django.contrib import admin

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    '''Admin View for Profile'''

    list_display = ['user', 'date_of_birth', 'photo']
    