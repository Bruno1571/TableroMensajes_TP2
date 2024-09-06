from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_mensaje, name='crear_mensaje'),
    path('recibidos/', views.mensajes_recibidos, name='mensajes_recibidos'),
    # otras URLs...
]
