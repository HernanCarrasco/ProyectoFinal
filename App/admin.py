from django.contrib import admin
from .models import *
from AppMensajes.models import *

admin.site.register(Blog)
admin.site.register(Mensaje)
admin.site.register(Avatar)

