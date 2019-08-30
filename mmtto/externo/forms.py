from django.forms import ModelForm
from django import forms
from .models import MantenimientoExterno

class ExternoForm(ModelForm):

    class Meta:
        model = MantenimientoExterno
        fields = "__all__"
        widgets = {
        'Modelo_Equipo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Modelo'}),
        'Inventario': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N°Inventario'}),
        'Serie': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N° Serie'}),
        'Numero': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N° Serie'}),
        'Marca': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Marca'}),
        'Tecnico': forms.TextInput(attrs={'class':'form-control', 'placeholder':'"Nombre del Tecnico"'}),
        'Empresa': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre de la Empresa'}),
        'Nombre_Equipo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del Equipo'}),
        'Unidad': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Servicio'}),
        'Observaciones': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Justificacion'}),
        'Detalle': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Detalles'}), 
        'Fecha': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }