from django.urls import path
from . import views

urlpatterns = [
    path('employees/',views.employees_view.as_view()),
    path('employees/<int:pk>/',views.employees_detail.as_view()),
    ]