from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'titulo_tag', 'autor', 'cuerpoPost')

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sin titulo'}),
            'titulo_tag':  forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sin tag'}),
            'autor':  forms.Select(attrs={'class': 'form-control'}),
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