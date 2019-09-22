from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import monitoreo
from .forms import MonitoreoForm
from django.shortcuts import get_object_or_404



class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)
###############Filtros################################
class FilterAmbulanciaListView(ListView):
    model = monitoreo
    paginate_by = 50
    queryset = monitoreo.objects.filter(nombre='Ambulancia')

class FilterDesfibriladorListView(ListView):
    model = monitoreo
    paginate_by = 50
    queryset = monitoreo.objects.filter(nombre='Desfibrilador')

class FilterIncubadoraListView(ListView):
    model = monitoreo
    paginate_by = 50
    queryset = monitoreo.objects.filter(nombre='Incubadora Fija/Transporte')

class FilterOximetroListView(ListView):
    model = monitoreo
    paginate_by = 50
    queryset = monitoreo.objects.filter(nombre='Oximetro de Pulso')

class FilterVentiladorListView(ListView):
    model = monitoreo
    paginate_by = 50
    queryset = monitoreo.objects.filter(nombre='Ventilador Mecanico')

class FilterVitalListView(ListView):
    model = monitoreo
    paginate_by = 50
    queryset = monitoreo.objects.filter(nombre='Monitor de Signos Vitales')
class FilterMonitoreoListView(ListView):
    model = monitoreo
    paginate_by = 50
    queryset = monitoreo.objects.filter(nombre='Monitor Multiparametro')

class FilterMonitoreoAnestesiaListView(ListView):
    model = monitoreo
    paginate_by = 50
    queryset = monitoreo.objects.filter(nombre='Maquina de Anestesia')

class FiltroMonitoreoListView(ListView):
    model = monitoreo
    paginate_by = 50
    def get_queryset(self):
        filter_val = self.request.GET.get('buscar')
        if filter_val == "":
            return monitoreo.objects.all()
        else:
            queryset =  monitoreo.objects.filter(inventario= filter_val)
            return queryset

################Termino de Filtros#######################
class MonitoreoListView(ListView):
    model = monitoreo
    paginate_by = 50
    

@method_decorator(staff_member_required, name='dispatch')
class MonitoreoCreate(CreateView):
    model = monitoreo
    form_class = MonitoreoForm
    success_url = reverse_lazy('monitores:monitores')
    def form_valid(self, form):
        response= super().form_valid(form)
        form.instance.nombre='Monitor Multiparametro'
        form.instance.save()
        return response
      

class MonitoreoDetailView(DetailView):
    model = monitoreo
