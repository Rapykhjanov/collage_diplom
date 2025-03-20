from django.contrib import admin
from .models import Student, HealthRecord


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'image')


class HealthRecordAdmin(admin.ModelAdmin):
    list_display = ('student', 'get_student_age', 'height', 'weight', 'blood_type', 'temperature', 'date')

    def get_student_age(self, obj):
        return obj.student.age  # Получаем возраст ученика через связь

    get_student_age.short_description = 'Возраст'  # Название колонки в админке


admin.site.register(Student, StudentAdmin)
admin.site.register(HealthRecord, HealthRecordAdmin)
