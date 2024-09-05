from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_mensaje, name='crear_mensaje'),
    # otras URLs...
]
