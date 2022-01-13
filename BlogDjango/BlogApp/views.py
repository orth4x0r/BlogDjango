from typing import List
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Categoria, Post
from .forms import PostForm, EditForm

# Create your views here
#def home(request):
#    return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-fechaPost']
    cats=Categoria.objects.all()

    def get_context_data(self, *args, **kwargs):
        cat_menu = Categoria.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'viewPost.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'addPost.html'
    #fields = '__all__'
    
class AddCategoryView(CreateView):
    model = Categoria
    form_class = PostForm
    template_name = 'addCategory.html'
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

def VerCategoria(request, cats): 
    category_posts = Post.objects.filter(categoria_post=cats.replace)
    return render(request, 'categorias.html', {'cats':cats.replace, 'category_posts':category_posts})

def AboutUsView(request):
    return render(request, 'about.html', {})