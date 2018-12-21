from django.urls import path

from .views import SignUpView, ProfileUpdate

urlpatterns = [
    # Registro
    path('signup/', SignUpView.as_view(), name='signup'),
    # Perfil de usuario
    path('profile/', ProfileUpdate.as_view(), name='profile')

]
