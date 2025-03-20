from django.shortcuts import render, get_object_or_404
from .models import Student

def home(request):
    return render(request, 'home.html')

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students_list': students})

def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'student_detail.html', {'student': student})

def student_page(request):
    return render(request, 'student.html')

def health_form(request):
    return render(request, 'health_form.html')

def success_page(request):
    return render(request, 'success.html')

def health_statistics(request):
    return render(request, 'statistics.html')
