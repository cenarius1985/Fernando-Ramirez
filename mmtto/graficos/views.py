from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class GraficosView(TemplateView):

    template_name = "graficos/grafico.html"