from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.student_list, name='student_list'),
    path('student/<int:student_id>/', views.student_detail, name='student_detail'),
    path('add/', views.health_form, name='health_form'),
    path('success/', views.success_page, name='success'),
    path('statistics/', views.health_statistics, name='health_statistics'),
]
