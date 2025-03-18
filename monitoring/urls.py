from django.urls import path
from . import views  # <-- Используем views

urlpatterns = [
    path('', views.health_form, name='health_form'),
    path('success/', views.success_page, name='success'),
    path('statistics/', views.health_statistics, name='health_statistics'),
]
