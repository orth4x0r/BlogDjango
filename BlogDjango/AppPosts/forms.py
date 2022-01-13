from django import forms
import datetime

class NewPost(forms.Form):
    titulo = forms.CharField(required=True)
    fecha = forms.DateField(initial=datetime.date.today)
    texto = forms.CharField(required=True)
    imagen = forms.ImageField(required=False)