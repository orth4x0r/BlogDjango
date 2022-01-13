from django.urls import path
from AppPosts import views
from .views import misPosts, bienvenidaPosts

urlpatterns = [

    path('', views.bienvenida, name="Inicio"),
    path('nosotrxs', views.nosotrxs, name="Nosotrxs"),
    path('mis-posts', misPosts.as_view(), name="Mis-posts"),
    path('bienvenida', bienvenidaPosts.as_view(), name="Bienvenida"),
    path('nuevo-post', views.nuevoPost, name="Nuevo-post"),
]