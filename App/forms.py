from django import forms

class UsuarioForm(forms.Form):
    nombre_usuario = forms.CharField(max_length=100)
    contraseña = forms.CharField(max_length=50)
    email = forms.EmailField(max_length = 254)

    def __str__(self):
        return self.nombre_usuario


class BlogForm(forms.Form):
    titulo = forms.CharField(max_length=100)
    subtitulo = forms.CharField(max_length=50)
    cuerpo = forms.CharField(max_length=5000)
    autor = forms.CharField(max_length=100)
    fecha_pub = forms.CharField(max_length=50)
    categoria = forms.CharField(max_length=50)
    img = forms.ImageField() ## Esto no se si va así, lo dejo mientras

    def __str__(self):
        return self.titulo

""" class Avatar(forms.Form):
    user = forms.ForeignKey(Usuario, on_delete=forms.CASCADE)
    imagen = forms.ImageField(upload_to='avatares', null=True, blank=True) ## Esto no se si va aquí, lo dejo comentado mientras"""


class ComentarioForm(forms.Form):
    cuerpo = forms.CharField(max_length=500)
    autor = forms.CharField(max_length=100)
    fecha_pub = forms.CharField(max_length=50)
