from django.db import models

class HealthRecord(models.Model):
    student_name = models.CharField(max_length=100)  # Имя ученика
    age = models.IntegerField()  # Возраст
    temperature = models.FloatField()  # Температура
    symptoms = models.TextField(blank=True)  # Симптомы
    date = models.DateTimeField(auto_now_add=True)  # Дата записи

    def __str__(self):
        return f"{self.student_name} - {self.date.strftime('%Y-%m-%d')}"
