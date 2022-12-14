from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from tinymce.widgets import TinyMCE


class UsuarioRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirme la contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField()
    password1= forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)
    first_name=forms.CharField(label='Modificar Nombre')
    last_name=forms.CharField(label='Modificar Apellido')

    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2', 'first_name', 'last_name']
        help_texts = {k:"" for k in fields}   


class BlogForm(forms.Form):
    titulo = forms.CharField(max_length=100)
    subtitulo = forms.CharField(max_length=300)
    cuerpo = forms.CharField(widget=TinyMCE(attrs={'cols':80, 'rows':30}))
    autor = forms.CharField(max_length=100)
    fecha_pub = forms.CharField(max_length=50)
    categoria = forms.CharField(max_length=50)
    img = forms.ImageField(label="Imagen") ## Esto no se si va así, lo dejo mientras

    def __str__(self):
        return self.titulo

class AvatarForm(forms.Form):
    imagen = forms.ImageField(label="Imagen")


