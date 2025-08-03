from django.urls import path
from . import views

urlpatterns = [
    path('Family',views.family_view.as_view()),
    path('Family/<int:pk>',views.family_detail.as_view()),  
]
