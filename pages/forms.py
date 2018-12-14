# clase de formularios para heredar.
from django import forms
# Modelo Page
from .models import Page


class PageForm(forms.ModelForm):
    class Meta:
        model = Page

        # fields = ['title', 'content', 'order']
        # Hace referencia a todos los campos del modelo, apareceran en orden de acuerdo al modelo
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Titulo'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'order': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Orden'})
        }

        labels = {
            'title': '',
            'content': '',
            'order': ''
        }
