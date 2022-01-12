from django import forms
from .models import Post, Categoria
cats= Categoria.objects.all().values_list('nombre', 'nombre')
cats_lista =[]

for item in cats:
    cats_lista.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'titulo_tag', 'autor', 'categoria_post', 'cuerpoPost', 'header_image')

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sin titulo'}),
            'titulo_tag':  forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sin tag'}),
            'autor':  forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'usernameCheck', 'type':'hidden'}),
            'categoria_post':  forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sin tag'}),
            'cuerpoPost':  forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Sin texto'}),

        }
        
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'titulo_tag', 'cuerpoPost')

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sin titulo'}),
            'titulo_tag':  forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sin tag'}),
#            'autor':  forms.Select(attrs={'class': 'form-control'}),
            'cuerpoPost':  forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Sin texto'}),

        }