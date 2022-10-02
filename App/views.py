from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from App.forms import * 


def inicio(request):
    return render (request, "App/inicio.html")
    
def post(request):
    return render (request, "App/BlogPost.html")

def crear_blog(request):

    if request.method == "POST":

        formulario_user = BlogForm(request.POST)

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
            return render (request, "App/inicio.html", {'mensaje': "Blog publicado!"})
        else:
            return render (request, "App/crear_blog.html", {"formulario":formulario_user, 'mensaje': "Error en los datos"}) 
    else:
        formulario_user=BlogForm()
        return render (request, "App/crear_blog.html", {"formulario":formulario_user})

