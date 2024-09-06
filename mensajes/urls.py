from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_mensaje, name='crear_mensaje'),
    path('recibidos/', views.mensajes_recibidos, name='mensajes_recibidos'),
    path('enviados/', views.mensajes_enviados, name='mensajes_enviados'),
    # otras URLs...
]
