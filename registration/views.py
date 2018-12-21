from django.urls import reverse_lazy

# Modelo 'Profile'
from .models import Profile

# Decoradores
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Vista Generica 'CreateView'
from django.views.generic import CreateView, TemplateView, UpdateView

# Email field (Modelo de formularios)
from .forms import UserCreationFormWithEmail
from .forms import ProfileForm

from django import forms


class SignUpView(CreateView):
    form_class = UserCreationFormWithEmail
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    # Obtener el formulario.
    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()

        # Modificar en tiempo real
        form.fields['username'].widget = forms.TextInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Nombre de usuario'})
        form.fields['email'].widget = forms.TextInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Direccion de Correo'})
        form.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Repite la contraseña'})

        return form


@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    template_name = 'registration/profile_form.html'
    #fields = ['avatar', 'bio', 'link']
    form_class = ProfileForm
    success_url = reverse_lazy('profile')

    # Overide, obtener objeto del usuario logeado.
    def get_object(self, queryset=None):
        # recuperar objeto que se va a editar(si no existe, lo crea)
        profile, created = Profile.objects.get_or_create(user=self.request.user)

        return profile
