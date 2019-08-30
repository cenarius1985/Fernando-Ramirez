from django.urls import path
from .views import InventarioListView, InventarioDetailView, InventarioCreate

urlpatterns = [
    path('inventario/', InventarioListView.as_view(), name='inventario'),
    path('create_inventario/', InventarioCreate.as_view(), name='create_inventario'),
    path('<int:pk>/', InventarioDetailView.as_view(), name='equipo'),
    
]