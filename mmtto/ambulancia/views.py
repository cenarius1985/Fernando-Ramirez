from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import ParqueAutomotriz
from .forms import AmbulanciaForm

class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Vistas Monitores

@method_decorator(staff_member_required, name='dispatch')
class MovilCreate(CreateView):
    model = ParqueAutomotriz
    form_class = AmbulanciaForm
    success_url = reverse_lazy('ambulancias:listaambulancia')

class AmbulanciaDetailView(DetailView):
    model = ParqueAutomotriz

# Create your views here.
class AmbulanciaListView(ListView):
    model = ParqueAutomotriz
    paginate_by = 50
