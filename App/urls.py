from django.urls import path    
from App.views import *

urlpatterns = [
        path("", inicio, name="inicio"),
        path("ver_post/<id>", ver_post, name="ver_post"),
        path("crear_blog/", crear_blog, name="crear_blog"),
        path("editar_blog/<id>", editar_blog, name="editar_blog"),
        path("pages/", pages, name="pages"),
        path("principal/", publicacion, name="principal"),
        path("busqueda_titulo/", busqueda_titulo , name="busqueda_titulo"),
        path("eliminar_blog/<id>", eliminar_blog , name="eliminar_blog"),
# Login, Register, Logout
        path("login", login_request, name="login"),
        path("register", register, name="register"),
]

"""cvb
        path("Usuarios/list/", UsuarioList.as_view(), name="usuario_lista"),
        path("Usuario/<pk>", UsuarioDetalle.as_view(), name="ver_usuario"),
        path("Usuario/editar/<pk>", UsuarioUpdate.as_view(), name="editar_usuario"),
        path("Usuario/eliminar/<pk>", UsuarioDelete.as_view(), name="eliminar_usuario"),"""