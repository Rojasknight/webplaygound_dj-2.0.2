from django import forms

#Modelo del formulario de usuario de django
from django.contrib.auth.forms import UserCreationForm

#modelo de Usuario de Django
from django.contrib.auth.forms import User


class UserCreationFormWithEmail(UserCreationForm):

    email = forms.EmailField(required=True, help_text='Requerido,254 caracteres como maximo y debe ser válido')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El email ya está registrado, prueba con otro!')
        return email