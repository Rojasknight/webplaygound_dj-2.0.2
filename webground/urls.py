from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),
    path('pages/', include('pages.urls')),
    path('admin/', admin.site.urls),


    #Rutas de autenticacion
    #Login
    path('accounts/', include('django.contrib.auth.urls')),
    #Register
    path('accounts/', include('registration.urls'))
]
