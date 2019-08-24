from django.urls import path
from .views import MonitoreoListView, MonitoreoCreate, MonitoreoDetailView

monitores_patterns = ([
    path('', MonitoreoListView.as_view(), name='monitores'),
    path('create_monitor/', MonitoreoCreate.as_view(), name='create1'),
    path('<int:pk>/<slug:slug>/', MonitoreoDetailView.as_view(), name='monitor'),
], 'monitores')