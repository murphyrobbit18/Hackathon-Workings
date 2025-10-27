from django.contrib import admin
from .models import PatientIntake, SOAPNote

@admin.register(PatientIntake)
class PatientIntakeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'dob', 'submitted_at', 'reviewed_by')

@admin.register(SOAPNote)
class SOAPNoteAdmin(admin.ModelAdmin):
    list_display = ('patient', 'physician', 'created_at')
