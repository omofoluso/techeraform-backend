from django.contrib import admin
from .models import ProgramApplication

# Register your models here.
@admin.register(ProgramApplication)
class ProgramApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'email', 'phone_number', 'program', 'gender')