from django.shortcuts import render
from .models import MantenimientoExterno
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .forms import ExternoForm

class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class ExternoListView(ListView):
    model = MantenimientoExterno
    form_class = ExternoForm
    paginate_by = 50
    
class ExternoDetailView(DetailView):
    model = MantenimientoExterno
    template_name= 'externo/MantenimientoExterno_detail.html'

@method_decorator(staff_member_required, name='dispatch')
class ExternoCreate(CreateView):
    model = MantenimientoExterno
    form_class= ExternoForm
    success_url = reverse_lazy('externolistview')
# filtro de busqueda por inventario

class FiltroExternoListView(ListView):
    model = MantenimientoExterno
    template_name= 'externo/MantenimientoExterno_list.html'
    paginate_by = 50
    def get_queryset(self):
        filter_val = self.request.GET.get('buscar')
        if filter_val == "":
            return MantenimientoExterno.objects.all()
        else:
            queryset =  MantenimientoExterno.objects.filter(Inventario= filter_val)
            return queryset