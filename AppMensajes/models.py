from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Mensaje(models.Model):
    cuerpo = HTMLField()
    autor = models.CharField(max_length=100) #Falta probar y mejorar esto, no se si funciona
    receptor = models.CharField(max_length=100) #Falta probar y mejorar esto, no se si funciona
