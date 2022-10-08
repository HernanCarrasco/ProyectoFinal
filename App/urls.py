from django.urls import path    
from App.views import *

urlpatterns = [
        path("", inicio, name="inicio"),
        path("ver_post/", ver_post, name="ver_post"),
        path("crear_blog/", crear_blog, name="crear_blog"),
        path("pages/", pages, name="pages"),
        path("principal", publicacion, name="principal"),
        path("busqueda_tema", busqueda , name="busqueda_tema"),
        path("crear_usuario", usuario , name="crear_usuario"),
]