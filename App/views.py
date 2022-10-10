from django.shortcuts import render
from .models import *
from App.forms import * 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required




def inicio(request):
    if request.user.is_authenticated:
        return render (request, "App/inicio.html", {"avatar": get_avatar(request)})
    else:
        return render (request, "App/inicio.html")


def login_request(request):
    if request.method == "POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu=request.POST["username"]
            clave=request.POST["password"]

            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, "App/inicio.html", {"mensaje_login": f"{usuario.username}", 'avatar': get_avatar(request)})
            else:
                return render(request, "App/login.html", {"formulario":form, "mensaje":"Usuario o Contraseña no existen"})
        else:
            return render(request, "App/login.html", {"formulario":form, "mensaje":"Usuario o Contraseña Incorrectos"})
    else:
        form=AuthenticationForm()
        return render(request, "App/login.html", {"formulario":form})


def register(request):
    if request.method=="POST":
        form=UsuarioRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            form.save()
            return render(request, "App/inicio.html", {"mensaje":f"Usuario {username} creado correctamente."})
        else:
            return render(request, "App/register.html", {"formulario":form, "mensaje":"Formulario Invalido"})

    else:
        form=UsuarioRegisterForm()
        return render(request, "App/register.html", {"formulario":form})

def mi_perfil(request):
    usuario=request.user
    lista_avatar=Avatar.objects.filter(user=usuario)
    if len(lista_avatar)!=0:
        avatar_usu=lista_avatar[0].imagen.url
    else:
        avatar_usu="/media/avatares/avatarpordefecto.jpg"
    return render(request, "App/mi_perfil.html", {'usuario':usuario, "avatar_usu": avatar_usu, 'avatar': get_avatar(request)})

@login_required
def eliminar_usuario(request, id):
    usuario=User.objects.get(id=id)
    usuario.delete()

    usuarios=User.objects.all() 
    return render(request, "App/usuarios.html", {'usuarios':usuarios, "avatar": get_avatar(request)})


@login_required
def editar_usuario(request):
    usuario=request.user
    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.save()
            return render(request, "App/inicio.html", {"mensaje":"Usuario editado correctamente"})
        else:
            return render(request, "App/editar_usuario.html", {"formulario":form, "usuario":usuario, "mensaje":"Formulario Invalido"})
    else:
        form= UserEditForm(instance=usuario)
    return render(request, "App/editar_usuario.html", {"formulario":form, "usuario":usuario, "avatar": get_avatar(request)})


@login_required
def agregar_avatar(request):
    if request.method=='POST':
        formulario=AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            avatar_pre=Avatar.objects.filter(user=request.user)
            if(len(avatar_pre)>0):
                avatar_pre[0].delete()
            avatar=Avatar(user=request.user, imagen=formulario.cleaned_data['imagen'])
            avatar.save()
            return render(request, 'App/inicio.html', {'usuario':request.user, 'mensaje':'Avatar agregado con exito.', "avatar": avatar.imagen.url})
        else:
            return render(request, 'App/agregar_avatar.html', {'formulario':formulario, 'mensaje':'Formulario Invalido'})
        
    else:
        formulario=AvatarForm()
        return render(request, "App/agregar_avatar.html", {"formulario":formulario, "usuario":request.user, "avatar": get_avatar(request)})


def get_avatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        imagen=lista[0].imagen.url
    else:
        imagen="/media/avatares/avatarpordefecto.jpg"
    return imagen




def ver_post(request, id):
    post = Blog.objects.get(id=id)
    return render(request, 'App/BlogPost.html', {'post': post})


@login_required
def crear_blog(request):

    if request.method == "POST":

        formulario_user = BlogForm(request.POST, request.FILES)

        if formulario_user.is_valid():
            info=formulario_user.cleaned_data
            tit=info["titulo"]
            subt=info["subtitulo"]
            cuerpo=info["cuerpo"]
            aut=info["autor"]
            fecha=info["fecha_pub"]
            cat=info["categoria"]
            img=info["img"]
            blog=Blog(titulo=tit, subtitulo=subt, cuerpo=cuerpo, autor=aut, fecha_pub=fecha, categoria=cat, img=img)
            blog.save()
            blogs=Blog.objects.all()
            return render (request, "App/pages.html", {'mensaje':"Blog publicado!", 'blogs':blogs})
        else:
            return render (request, "App/crear_blog.html", {"formulario":formulario_user, 'mensaje': "Error en los datos"}) 
    else:
        formulario_user=BlogForm()
        return render (request, "App/crear_blog.html", {"formulario":formulario_user, "avatar": get_avatar(request)})
        
@login_required
def editar_blog(request, id):

    blog = Blog.objects.get(id=id)

    if request.method == "POST":

        formulario_user = BlogForm(request.POST, request.FILES)

        if formulario_user.is_valid():
            info=formulario_user.cleaned_data
            blog.titulo=info["titulo"]
            blog.subtitulo=info["subtitulo"]
            blog.cuerpo=info["cuerpo"]
            blog.autor=info["autor"]
            blog.fecha_pub=info["fecha_pub"]
            blog.categoria=info["categoria"]
            blog.img=info["img"]
            blog.save()
            blogs=Blog.objects.all()
            return render (request, "App/pages.html", {'mensaje': "Blog actualizado!", 'blogs':blogs, "avatar": get_avatar(request)})
        else:
            return render (request, "App/editar_blog.html", {"formulario":formulario_user, 'mensaje': "Error en los datos","avatar": get_avatar(request)}) 
    else:
        formulario_user=BlogForm(initial={'titulo':blog.titulo, 'subtitulo':blog.subtitulo, 'cuerpo':blog.cuerpo, 'autor':blog.autor, 'fecha_pub':blog.fecha_pub, 'categoria':blog.categoria, 'img':blog.img})
        return render (request, "App/editar_blog.html", {"formulario":formulario_user, 'blog':blog, "avatar": get_avatar(request)})

@login_required
def pages(request):
    blogs=Blog.objects.all() 
    return render(request, "App/pages.html", {'blogs':blogs, "avatar": get_avatar(request)})


@login_required
def eliminar_blog(request, id):
    blog=Blog.objects.get(id=id)
    blog.delete()

    blogs=Blog.objects.all() 
    return render(request, "App/pages.html", {'blogs':blogs, "avatar": get_avatar(request)})



def busqueda_titulo(request):
    if request.GET['titulo']:
        blogs=Blog.objects.filter(titulo__icontains=request.GET['titulo'])             
        return render(request, "App/result_busqueda.html", {"blogs":blogs, "avatar": get_avatar(request)})
    else:
        return render(request, "App/result_busqueda.html", {'mensaje':"No se ingresó un titulo para la busqueda.", "avatar": get_avatar(request)})

def busqueda_cat(request):
        if request.GET['categoria']:
            blogs=Blog.objects.filter(categoria=request.GET['categoria'])             
            return render(request, "App/result_busqueda.html", {"blogs":blogs, "avatar": get_avatar(request)})
        else:
            return render(request, "App/result_busqueda.html", {'mensaje':"No se ingresó un titulo para la busqueda.", "avatar": get_avatar(request)})

def ver_usuario(request, id):
    user=User.objects.get(id=id)
    lista_avatar=Avatar.objects.filter(user=user)
    if len(lista_avatar)!=0:
        avatar_usu=lista_avatar[0].imagen.url
    else:
        avatar_usu="/media/avatares/avatarpordefecto.jpg"
    return render(request, "App/Usuario.html", {'user':user, "avatar_usu":avatar_usu, "avatar": get_avatar(request)}) 

@login_required
def usuarios_lista(request):
    usuarios=User.objects.all()
    if request.user.is_authenticated:
        return render(request, "App/usuarios.html", {'usuarios':usuarios, "avatar": get_avatar(request)})
    else:
        return render(request, "App/usuarios.html", {'usuarios':usuarios})






    

