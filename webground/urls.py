from django.contrib import admin
from django.urls import path, include

from django.conf import settings

urlpatterns = [
    path('', include('core.urls')),
    path('pages/', include('pages.urls')),
    path('admin/', admin.site.urls),

    # Rutas de autenticacion
    # Login
    path('accounts/', include('django.contrib.auth.urls')),
    # Register
    path('accounts/', include('registration.urls'))

]


# Configuración para el cargue de las Imagenes
if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
