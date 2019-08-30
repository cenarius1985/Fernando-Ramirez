from django.urls import path
from .views import MonitoreoListView, MonitoreoCreate, MonitoreoDetailView, FilterMonitoreoListView, FilterVitalListView, FilterVentiladorListView, FilterOximetroListView, FilterIncubadoraListView, FilterDesfibriladorListView, FilterAnestesiaListView, FilterAmbulanciaListView,FiltroMonitoreoListView

monitores_patterns = ([
    path('', MonitoreoListView.as_view(), name='monitores'),
    path('ambulancia_filter', FilterAmbulanciaListView.as_view(), name='filterambulancia'),
    
     path('anestesia_filter', FiltroMonitoreoListView.as_view(), name='filtroinventario'),
    path('anestesia_filter', FilterAnestesiaListView.as_view(), name='filteranestesia'),
    path('desfibrilador_filter', FilterDesfibriladorListView.as_view(), name='filterdesfibrilador'),
    path('incubadora_filter', FilterIncubadoraListView.as_view(), name='filterincubadora'),
    path('Monitor_oximetro', FilterOximetroListView.as_view(), name='filteroximetro'),
    path('Monitor_ventilador', FilterVentiladorListView.as_view(), name='filterventilador'),
    path('Monitor_Mult', FilterMonitoreoListView.as_view(), name='filtermonitor'),
    path('Monitor_Vital', FilterVitalListView.as_view(), name='filtervital'),
    path('create_monitor/', MonitoreoCreate.as_view(), name='create1'),
    path('<int:pk>/<slug:slug>/', MonitoreoDetailView.as_view(), name='monitor'),
], 'monitores')