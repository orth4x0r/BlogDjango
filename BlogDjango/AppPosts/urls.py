from django.urls import path
from AppPosts import views

urlpatterns = [

    path('', views.bienvenida, name="Inicio"),
    path('nosotrxs', views.nosotrxs, name="Nosotrxs"),
    path('mis-posts', views.misPosts, name="Mis-posts"),
    path('bienvenida', views.bienvenida, name="Bienvenida"),
    path('nuevo-post', views.nuevoPost, name="Nuevo-post"),
]