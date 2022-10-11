from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField



class Blog(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=300)
    cuerpo = HTMLField()
    autor = models.CharField(max_length=100)
    fecha_pub = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    img = models.ImageField(upload_to='blog_img', null=True, blank=True) 

    def __str__(self):
        return self.titulo


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)





