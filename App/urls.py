from django.urls import path, include    
from App.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
        path("", inicio, name="inicio"),
        path("ver_post/<id>", ver_post, name="ver_post"),
        path("crear_blog/", crear_blog, name="crear_blog"),
        path("editar_blog/<id>", editar_blog, name="editar_blog"),
        path("pages/", pages, name="pages"),
        path("busqueda_titulo/", busqueda_titulo , name="busqueda_titulo"),
        path("eliminar_blog/<id>", eliminar_blog , name="eliminar_blog"),
        path("Usuarios/lista/", usuarios_lista, name="usuarios_lista"),
        path("Usuario/<id>", ver_usuario, name="ver_usuario"),
        path("editar_usuario/", editar_usuario, name="editar_usuario"),
        path("agregar_avatar/", agregar_avatar, name="agregar_avatar"),
        path("busqueda_cat/", busqueda_cat, name="busqueda_cat"),
        path("mi_perfil/", mi_perfil, name="mi_perfil"),
        path('usuario/eliminar/<id>', eliminar_usuario, name='eliminar_usuario'),
        path('tinymce/', include('tinymce.urls')),
# Login, Register, Logout
        path("login/", login_request, name="login"),
        path("register/", register, name="register"),
        path("logout/", LogoutView.as_view(template_name='App/logout.html'), name="logout"),      
]