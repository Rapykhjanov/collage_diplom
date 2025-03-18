from django.shortcuts import render, redirect
from .forms import HealthRecordForm
import matplotlib.pyplot as plt
import io
import base64
from .models import HealthRecord


def health_form(request):
    if request.method == 'POST':
        form = HealthRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # После отправки перенаправляем
    else:
        form = HealthRecordForm()
    return render(request, 'monitoring/health_form.html', {'form': form})


def success_page(request):
    return render(request, 'monitoring/success.html')


# Добавляем health_statistics
def health_statistics(request):
    records = HealthRecord.objects.all()

    temperatures = [record.temperature for record in records]
    dates = [record.date.strftime('%Y-%m-%d') for record in records]

    plt.figure(figsize=(8, 4))
    plt.plot(dates, temperatures, marker='o', linestyle='-', color='b', label='Температура')
    plt.xlabel('Дата')
    plt.ylabel('Температура (°C)')
    plt.title('Изменение температуры учащихся')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    image_png = buffer.getvalue()
    buffer.close()
    graph = base64.b64encode(image_png).decode('utf-8')

    return render(request, 'monitoring/statistics.html', {'graph': graph})
