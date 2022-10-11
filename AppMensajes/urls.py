from django.urls import path, include    
from App.views import *
from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
        path("enviar_msg/", enviar_msg, name="enviar_msg"),
        path("mensajes/", mensajes, name="mensajes"),
]