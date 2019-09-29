from django.urls import path
from .views import MovilCreate, AmbulanciaDetailView, AmbulanciaListView

ambulancia_patterns = ([
    path('createambulancia/', MovilCreate.as_view(), name='crearambulancia'),
    path('ambulancia_lista/', AmbulanciaListView.as_view(), name='listaambulancia'),
    path('<int:pk>/ambulancia',AmbulanciaDetailView.as_view(), name='ambulancia'),
], 'ambulancias')