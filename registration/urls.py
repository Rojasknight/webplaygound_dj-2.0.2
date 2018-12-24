from django.urls import path

from .views import SignUpView, ProfileUpdate, EmailUpdate

urlpatterns = [
    # Registro
    path('signup/', SignUpView.as_view(), name='signup'),
    # Perfil de usuario
    path('profile/', ProfileUpdate.as_view(), name='profile'),
    # Perfil, editar email
    path('profile/email/', EmailUpdate.as_view(), name='profile_email')

]
