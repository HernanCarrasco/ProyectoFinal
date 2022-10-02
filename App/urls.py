from django.urls import path    
from App.views import *

urlpatterns = [
        path("", inicio, name="inicio"),
        path("post/", post, name="post"),
        path("crear_blog/", crear_blog, name="crear_blog")

]