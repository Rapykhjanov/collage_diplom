from django.contrib import admin
from .models import HealthRecord

@admin.register(HealthRecord)
class HealthRecordAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'age', 'temperature', 'date')
    search_fields = ('student_name',)
    list_filter = ('date', 'temperature')

