from django.urls import path,include
from . import views
urlpatterns = [
    path('teachers',views.teachers_view.as_view()),
    path('teachers/<int:pk>',views.teachers_detail.as_view()),

]