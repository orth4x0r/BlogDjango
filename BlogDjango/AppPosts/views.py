from django.shortcuts import render
from django.template import Context, Template, loader
from django.http import HttpResponse
from datetime import datetime

def Intro(request):
 
    return render(request, 'AppPosts/nosotrxs.html')

def BlogPosts(request):
    return render(request, 'AppPosts/tus_posts.html')