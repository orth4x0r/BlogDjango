from typing import List
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm

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

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'updatePost.html'
#    fields = ['titulo', 'titulo_tag', 'cuerpoPost']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'deletePost.html'
    success_url = reverse_lazy('home')