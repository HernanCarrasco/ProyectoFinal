from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from tinymce.widgets import TinyMCE





class MensajeForm(forms.Form):
    receptor = forms.CharField(max_length=100)
    cuerpo = forms.CharField(widget=TinyMCE(attrs={'cols':80, 'rows':30}))
    autor = forms.CharField(max_length=100) #Falta probar y mejorar esto, no se si funciona
    
