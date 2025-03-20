from django.shortcuts import render, redirect, get_object_or_404
from .forms import HealthRecordForm
from .models import Student, HealthRecord
import matplotlib.pyplot as plt
import io
import base64


def home(request):
    """Главная страница"""
    return render(request, 'monitoring/home.html')


def student_list(request):
    """Вывод списка учащихся"""
    students = Student.objects.all()
    return render(request, 'monitoring/student.html', {
        'students_list': students,
        'error': 'Нет данных о студентах!' if not students.exists() else None
    })


def student_detail(request, student_id):
    """Детальная информация о здоровье учащегося"""
    student = get_object_or_404(Student, id=student_id)
    health_record = HealthRecord.objects.filter(student=student).order_by('-date').first()

    return render(request, 'monitoring/student_detail.html', {
        'student': student,
        'student_health': health_record
    })


def health_form(request):
    """Форма для добавления медицинских записей"""
    if request.method == 'POST':
        form = HealthRecordForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = HealthRecordForm()
    return render(request, 'monitoring/health_form.html', {'form': form})


def success_page(request):
    """Страница успешного добавления записи"""
    return render(request, 'monitoring/success.html')


def health_statistics(request):
    """Статистика здоровья учащихся"""
    records = HealthRecord.objects.all()

    if not records.exists():
        return render(request, 'monitoring/statistics.html', {'graph': None, 'error': 'Нет данных для статистики!'})

    temperatures = [record.temperature for record in records if record.temperature is not None]
    dates = [record.date.strftime('%Y-%m-%d') for record in records if record.temperature is not None]

    if not temperatures:
        return render(request, 'monitoring/statistics.html', {'graph': None, 'error': 'Нет данных о температуре!'})

    plt.figure(figsize=(8, 4))
    plt.plot(dates, temperatures, marker='o', linestyle='-', color='b', label='Температура')
    plt.xlabel('Дата')
    plt.ylabel('Температура (°C)')
    plt.title('Динамика температуры учащихся')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    graph = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()

    return render(request, 'monitoring/statistics.html', {'graph': graph})
