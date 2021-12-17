from django.urls import path
from AppPosts import views

urlpatterns = [
 
    path('nosotrxs', views.Intro),
    path('posts/', views.blogposts),
    #path('ingresa/', views.ingresar()),
]