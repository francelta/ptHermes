from django.urls import path
from . import views

urlpatterns = [
    path('start-task/', views.start_tarea_pesada, name='start_tarea_pesada'),
]
