from django.template.context import RequestContext
from django.urls import path
from .views import Intro

urlpatterns = [
 
    path('nosotrxs/', Intro.as_view(), name='nosotrxs'),
    #path('posts/', views.blogposts()),
    #path('ingresa/', views.ingresar()),
]