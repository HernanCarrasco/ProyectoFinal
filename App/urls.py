from django.urls import path    
from App.views import *

urlpatterns = [
        path("", inicio, name="inicio"),
        path("ver_post/<id>", ver_post, name="ver_post"),
        path("crear_blog/", crear_blog, name="crear_blog"),
        path("editar_blog/<id>", editar_blog, name="editar_blog"),
        path("pages/", pages, name="pages"),
        path("principal/", publicacion, name="principal"),
        #path("busqueda/", busqueda , name="busqueda"),
        path("busqueda_titulo/", busqueda_titulo , name="busqueda_titulo"),
        path("crear_usuario/", usuario , name="crear_usuario"),
        path("eliminar_blog/<id>", eliminar_blog , name="eliminar_blog"),

]