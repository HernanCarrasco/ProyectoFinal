from django import forms


class UsuarioForm(forms.Form):
    nombre_usuario = forms.CharField(max_length=100)
    contraseña = forms.CharField(max_length=50)
    email = forms.EmailField(max_length = 254)

    def __str__(self):
        return self.nombre_usuario


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
