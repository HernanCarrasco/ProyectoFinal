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

    


def enviar_msg(request):
    if request.method == "POST":
        pass

        """formulario_user = BlogForm(request.POST, request.FILES)

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
            return render (request, "App/crear_blog.html", {"formulario":formulario_user, 'mensaje': "Error en los datos"}) """
    else:
        form_mensaje=MensajeForm()
        return render (request, "AppMensajes/crear_mensaje.html", {"formulario":form_mensaje, "avatar": get_avatar(request)})
    

