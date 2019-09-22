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
from monitoreo.urls import monitores_patterns
from oximetro.urls import oximetro_patterns
from ambulancia.urls import ambulancia_patterns
from anestesia.urls import anestesia_patterns
from desfibrilador.urls import desfibrilador_patterns
from incubadora.urls import incubadora_patterns
from ventilador.urls import ventilador_patterns
from vital.urls import vital_patterns



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('core.urls')),
    path('',include('registration.urls')),
    path('',include(pages_patterns)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
    path('profiles/', include(profiles_patterns)),
    path('monitores/', include(monitores_patterns)),
    # Paths de Formulario de Oximetro de Pulso
    path('oximetro/', include(oximetro_patterns)),
    # Paths de Formulario de Ambulancia
    path('ambulancia/', include(ambulancia_patterns)),
    # Paths de Formulario de Maquinas de Anestesia
    path('anestesia/', include(anestesia_patterns)),
    # Paths de Formulario de Desfibrilador
    path('desfibrilador/', include(desfibrilador_patterns)),
    path('', include('externo.urls')),
    # Paths de Formulario de Incubadora
    path('incubadora/', include(incubadora_patterns)),
    path('', include('inventario.urls')),
    # Paths de Formulario de ventiladores
    path('ventilador/', include(ventilador_patterns)),
    # Paths de Formulario de Monitor de Signos Vitales
    path('monitor_signos_vitales/', include(vital_patterns)),
    
]
admin.site.site_header="ADMINISTRADOR DE MANTENIMIENTO"