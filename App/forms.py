from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UsuarioRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirme la contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}


class BlogForm(forms.Form):
    titulo = forms.CharField(max_length=100)
    subtitulo = forms.CharField(max_length=300)
    cuerpo = forms.CharField(max_length=5000)
    autor = forms.CharField(max_length=100)
    fecha_pub = forms.CharField(max_length=50)
    categoria = forms.CharField(max_length=50)
    img = forms.ImageField(label="Imagen") ## Esto no se si va así, lo dejo mientras

    def __str__(self):
        return self.titulo

"""class Avatar(forms.Form):
    user = forms.ForeignKey(User, on_delete=forms.CASCADE)
    imagen = forms.ImageField(upload_to='avatares', null=True, blank=True) ## Esto no se si va aquí, lo dejo comentado mientras


class ComentarioForm(forms.Form):
    cuerpo = forms.CharField(max_length=500)
    avatar = forms.ForeignKey(Avatar, on_delete=models.CASCADE) #Falta probar y mejorar esto, no se si funciona
    autor = forms.ForeignKey(Usuario, on_delete=models.CASCADE) #Falta probar y mejorar esto, no se si funciona
    fecha_pub = forms.CharField(max_length=50)


class MensajeForm(forms.Form):
    cuerpo = forms.CharField(max_length=500)
    avatar = forms.ForeignKey(Avatar, on_delete=forms.CASCADE) #Falta probar y mejorar esto, no se si funciona
    autor = forms.ForeignKey(Usuario, on_delete=forms.CASCADE) #Falta probar y mejorar esto, no se si funciona
    fecha_pub = forms.CharField(max_length=50)"""
