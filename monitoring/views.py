from django.shortcuts import render

def home(request):
    return render(request, 'monitoring/home.html')

def health_form(request):
    return render(request, 'monitoring/health_form.html')

def student_list(request):
    return render(request, 'monitoring/student_list.html')

def student_detail(request, student_id):
    return render(request, 'monitoring/student_detail.html')

def health_statistics(request):
    return render(request, 'monitoring/statistics.html')

def success_page(request):
    return render(request, 'monitoring/success.html')
