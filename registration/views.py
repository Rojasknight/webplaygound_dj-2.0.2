from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Vista Generica 'CreateView'
from django.views.generic import CreateView

# Email field
from .forms import UserCreationFormWithEmail

from django import forms


class SignUpView(CreateView):

    form_class = UserCreationFormWithEmail
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    #Obtener el formulario.
    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()

        # Modificar en tiempo real
        form.fields['username'].widget = forms.TextInput(
            attrs={'class':'form-control mb-2', 'placeholder':'Nombre de usuario'})
        form.fields['email'].widget = forms.TextInput(
            attrs={'class':'form-control mb-2', 'placeholder':'Direccion de Correo'})
        form.fields['password1'].widget = forms.PasswordInput(
            attrs={'class':'form-control mb-2', 'placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(
            attrs={'class':'form-control mb-2', 'placeholder':'Repite la contraseña'})


        return form