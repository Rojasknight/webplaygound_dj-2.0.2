from django.urls import path

from .views import SignUpView


urlpatterns = [
    #Registro
    path('signup/', SignUpView.as_view(), name='signup')
]