from django.urls import reverse_lazy

# Modelo 'Profile'
from .models import Profile

# Decoradores
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Vista Generica 'CreateView'
from django.views.generic import CreateView, TemplateView, UpdateView

# Email field (Modelo de formularios)
from .forms import UserCreationFormWithEmail, EmailForm
from .forms import ProfileForm

# jango form
from django import forms


class SignUpView(CreateView):
    form_class = UserCreationFormWithEmail
    template_name = 'registration/signup.html'

    # override success url
    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    # getting form
    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()

        # Edit in real time (form)
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
    # fields = ['avatar', 'bio', 'link']
    form_class = ProfileForm
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        # Obtener objeto que se va a editar, y asignarselo al usuario que esta logeado
        profile, created = Profile.objects.get_or_create(user=self.request.user)

        return profile


@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
    template_name = 'registration/profile_email_form.html'
    form_class = EmailForm
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        # Obtener el usuario a editar
        return self.request.user

    def get_form(self, form_class=None):
        form = super(EmailUpdate, self).get_form()
        # Edit in real time (form)
        form.fields['email'].widget = forms.EmailInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Direccion de Correo'})

        return form