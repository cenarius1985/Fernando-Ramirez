from django.urls import path
from .views import ExternoCreate, ExternoDetailView, ExternoListView

urlpatterns = [
    path('externolista/', ExternoListView.as_view(), name='externolistview'),
    path('create_externo/', ExternoCreate.as_view(), name='createexterno'),
    path('<int:pk>/externo/', ExternoDetailView.as_view(), name='matenimientoexterno'),
    ]