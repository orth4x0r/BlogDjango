from typing import List
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm

# Create your views here
#def home(request):
#    return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'viewPost.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'addPost.html'
    #fields = '__all__'
