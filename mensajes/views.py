from django.shortcuts import render, redirect
from .models import Mensaje

def crear_mensaje(request):
    if request.method == 'POST':
        texto = request.POST.get('texto')
        remitente = request.POST.get('remitente')
        destinatario = request.POST.get('destinatario')

        if texto and remitente and destinatario:
            Mensaje.objects.create(
                texto=texto,
                remitente=remitente,
                destinatario=destinatario
            )
            return redirect('crear_mensaje')  # Redirige a la página principal
        else:
            error = "Todos los campos son requeridos."
            return render(request, 'crear_mensaje.html', {'error': error})

    return render(request, 'crear_mensaje.html')


def mensajes_recibidos(request):
    # Obtener el destinatario 
    destinatario = request.GET.get('destinatario', '')

    # Filtrar los mensajes que tienen el destinatario 
    if destinatario:
        mensajes = Mensaje.objects.filter(destinatario=destinatario)
    else:
        mensajes = Mensaje.objects.none()  

   
    return render(request, 'mensajes_recibidos.html', {'mensajes': mensajes})
