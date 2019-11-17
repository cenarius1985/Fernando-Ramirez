"""mmtto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pages.urls import pages_patterns
from profiles.urls import profiles_patterns
from messenger.urls import messenger_patterns
from django.conf import settings
from monitoreo.urls import monitores_patterns
from anestesia.urls import anestesia_patterns
from ambulancia.urls import ambulancia_patterns
from ventilador.urls import ventilador_patterns
from desfibrilador.urls import desfibrilador_patterns
from incubadora.urls import incubadora_patterns
from oximetro.urls import oximetro_patterns
from vital.urls import vital_patterns


urlpatterns = [
    path('', include('core.urls')),
    path('', include('inventario.urls')),
    path('', include('externo.urls')),
    path('pages/', include(pages_patterns)),
    # Paths de Formulario de Monitor de Signos Vitales
    path('monitor_signos_vitales/', include(vital_patterns)),
     # Paths de Formulario de Oximetro de Pulso
    path('oximetro/', include(oximetro_patterns)),
    # Paths de Formulario de Incubadora
    path('incubadora/', include(incubadora_patterns)),
    # Paths de Formulario de Desfibrilador
    path('desfibrilador/', include(desfibrilador_patterns)),
    # Paths de Formulario de ventiladores
    path('ventilador/', include(ventilador_patterns)),
    # Paths de Formulario de Ambulancia
    path('ambulancia/', include(ambulancia_patterns)),
     # Paths de Formulario de Maquinas de Anestesia
    path('anestesia/', include(anestesia_patterns)),
    # Paths de Formulario Monitores
    path('monitores/', include(monitores_patterns)),
    path('admin/', admin.site.urls),
    # Paths de Auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
    # Paths de profiles
    path('profiles/', include(profiles_patterns)),
    # Paths de Messenger
    path('messenger/', include(messenger_patterns)),
    
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# MODIFICAR ADMINISTRADOR
admin.site.site_header="ADMINISTRADOR DE MANTENIMIENTO"