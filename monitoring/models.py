from django.db import models

class Student(models.Model):
    """Модель учащегося"""
    name = models.CharField(max_length=100)  # Имя учащегося
    age = models.IntegerField()  # Возраст
    image = models.ImageField(upload_to='students/', blank=True, null=True)  # Фото учащегося

    def __str__(self):
        return self.name

class HealthRecord(models.Model):
    """Модель медицинской записи учащегося"""
    student = models.ForeignKey(
        Student,
        on_delete=models.SET_NULL,
        related_name='health_records',
        null=True, blank=True  # Разрешаем пустые значения, чтобы избежать ошибки
    )
    height = models.FloatField(blank=True, null=True)  # Рост в см (может быть пустым)
    weight = models.FloatField(blank=True, null=True)  # Вес в кг (может быть пустым)
    blood_type = models.CharField(
        max_length=3,
        choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')],
        blank=True, null=True  # Теперь можно оставить пустым
    )
    temperature = models.FloatField(blank=True, null=True)  # Температура
    symptoms = models.TextField(blank=True, null=True)  # Симптомы или жалобы
    medical_notes = models.TextField(blank=True, null=True)  # Медицинские примечания
    health_report = models.FileField(upload_to='health_reports/', blank=True, null=True)  # Медицинский отчет
    date = models.DateTimeField(auto_now_add=True)  # Дата записи

    def __str__(self):
        return f"{self.student.name if self.student else 'Неизвестный'} - {self.date.strftime('%Y-%m-%d')}"
