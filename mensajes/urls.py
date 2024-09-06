from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_mensaje, name='crear_mensaje'),
    path('recibidos/', views.mensajes_recibidos, name='mensajes_recibidos'),
    path('enviados/', views.mensajes_enviados, name='mensajes_enviados'),
    path('eliminar/<int:pk>/', views.EliminarMensajeView.as_view(), name='eliminar_mensaje'),
    # otras URLs...
]
