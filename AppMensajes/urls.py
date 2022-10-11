from django.urls import path, include    
from App.views import *
from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
        path("enviar_msg/", enviar_msg, name="enviar_msg"),
        path("mensajes/", mensajes, name="mensajes"),
        path("ver_mensajes_rec/", ver_mensajes_rec, name="ver_mensajes_rec"),
        path("ver_mensajes_env/", ver_mensajes_env, name="ver_mensajes_env"),
        path("eliminar_mensaje/<id>", eliminar_mensaje, name="eliminar_mensaje"),
]