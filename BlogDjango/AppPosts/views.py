from django import template
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.template.context import RequestContext
from django.utils import text
from django.template import Context, Template, loader
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse
from datetime import datetime
from .models import Post
from .forms import *

def nosotrxs(request):
    return render(request, 'AppPosts/nosotrxs.html')

class misPosts(ListView):
    model = Post
    template_name = "AppPosts/mis_posts.html"
    context_object_name = "listaPosts"
    queryset = Post.objects.all()

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = Post.objects.all()
        return context

class bienvenidaPosts(ListView):
    model = Post
    template_name = "AppPosts/bienvenida.html"
    context_object_name = "listaPosts"

    def get_queryset(self):
        qs = super().get_queryset().filter()[:3]
        return qs

def bienvenida(request):
    return render(request, 'AppPosts/bienvenida.html')

def nuevoPost(request):

    if request.method == "POST":

        nuevoPost = NewPost(request.POST)

        if nuevoPost.is_valid():
            informacion = nuevoPost.cleaned_data
            newPost = Post(titulo=informacion["titulo"],autor=informacion["autor"],fecha=informacion["fecha"],texto=informacion["texto"],imagen=informacion["imagen"])
            newPost.save()

        return render(request, 'AppPosts/mis_posts.html')

    else:
        nuevoPost = NewPost()
    return render(request, 'AppPosts/nuevo_post.html', {"nuevoPost":nuevoPost})
