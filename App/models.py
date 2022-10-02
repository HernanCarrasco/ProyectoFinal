from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=50)
    email = models.EmailField(max_length = 254)

    def __str__(self):
        return self.nombre_usuario


class Blog(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=50)
    cuerpo = models.CharField(max_length=5000)
    autor = models.CharField(max_length=100)
    fecha_pub = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    img = models.ImageField() ## Esto no se si va así, lo dejo mientras

    def __str__(self):
        return self.titulo

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True) ## Esto no se si va así, lo dejo mientras


class Comentario(models.Model):
    cuerpo = models.CharField(max_length=500)
    autor = models.CharField(max_length=100)
    fecha_pub = models.CharField(max_length=50)
