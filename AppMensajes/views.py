from django.shortcuts import render
from App.models import *
from App.forms import * 
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import * 
from App.views import get_avatar

@login_required
def mensajes(request):
    return render (request, "AppMensajes/mensajes_home.html", {"avatar": get_avatar(request)})

@login_required
def enviar_msg(request):
    usuario=request.user
    if request.method == "POST":
        form_mensaje = MensajeForm(request.POST, request.FILES)
        if form_mensaje.is_valid():
            info=form_mensaje.cleaned_data
            receptor=info["receptor"]
            cuerpo=info["cuerpo"]
            aut=info["autor"]
            mensaje=Mensaje(receptor=receptor, cuerpo=cuerpo, autor=aut)
            mensaje.save()
            mensajes= Mensaje.objects.filter(autor__icontains=usuario.username)
            return render (request, "AppMensajes/ver_mensajes_env.html", {'mensaje':"Mensaje enviado!", 'mensajes':mensajes})
        else:
            return render (request, "AppMensajes/crear_mensaje.html", {"formulario":form_mensaje, 'mensaje': "Error en los datos"})
    else:
        form_mensaje=MensajeForm()
        return render (request, "AppMensajes/crear_mensaje.html", {"formulario":form_mensaje, "avatar": get_avatar(request)})
    
@login_required
def ver_mensajes_rec(request):
    usuario=request.user
    mensajes= Mensaje.objects.filter(receptor__icontains=usuario.username) #si hay error puede que sea aqui, dejar usuario o poner request.get como en la view de busqueda
    return render (request, "AppMensajes/ver_mensajes_rec.html", {"mensajes":mensajes, "avatar": get_avatar(request)})


@login_required
def ver_mensajes_env(request):
    usuario=request.user
    mensajes= Mensaje.objects.filter(autor__icontains=usuario.username) #si hay error puede que sea aqui, dejar usuario o poner request.get como en la view de busqueda
    return render (request, "AppMensajes/ver_mensajes_env.html", {"mensajes":mensajes, "avatar": get_avatar(request)})


@login_required
def eliminar_mensaje(request, id):
    usuario=request.user
    mensaje=Mensaje.objects.get(id=id)
    mensaje.delete()
    mensajes= Mensaje.objects.filter(receptor__icontains=usuario.username) 
    return render(request, "AppMensajes/mensajes_home.html", {'mensajes':mensajes, "avatar": get_avatar(request)})


