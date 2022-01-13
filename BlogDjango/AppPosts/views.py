from django.shortcuts import render
from django.template import Context, Template, loader
from django.http import HttpResponse
from datetime import datetime
from AppPosts.models import *
from AppPosts.forms import *

def nosotrxs(request):
    return render(request, 'AppPosts/nosotrxs.html')

def misPosts(request):
    return render(request, 'AppPosts/mis_posts.html')

def bienvenida(request):
    return render(request, 'AppPosts/bienvenida.html')

def nuevoPost(request):

    if request.method == "POST":

        nuevoPost = NewPost(request.POST)

        if nuevoPost.is_valid():
            informacion = nuevoPost.cleaned_data
            newPost = Post(titulo=informacion["titulo"],fecha=informacion["fecha"],texto=informacion["texto"],imagen=informacion["imagen"])
            newPost.save()

        return render(request, 'AppPosts/mis_posts.html')

    else:
        nuevoPost = NewPost()
    return render(request, 'AppPosts/nuevo_post.html', {"nuevoPost":nuevoPost})

