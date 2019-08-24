from django.shortcuts import render
from .models import inventario
from django.views.generic.list import ListView

# Create your views here.
class InventarioListView(ListView):
    model = inventario