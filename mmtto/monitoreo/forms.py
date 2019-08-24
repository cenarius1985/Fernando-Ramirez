from django.forms import ModelForm
from django import forms
from .models import monitoreo

class MonitoreoForm(ModelForm):

    class Meta:
        model = monitoreo
        fields = ['responsable','tecnico2','tecnico1','servicio', 'nombre','marca', 'serie','inventario', 'modelo','justificacion','fecha', 'pauta1', 'pauta2', 'pauta3','pauta4','pauta5','pauta6','pauta7','pauta8','pauta9','pauta10','pauta11','pauta12','pauta13','pauta14','pauta15']
        widgets = {
        
        'modelo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Modelo'}),
        'inventario': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N°Inventario'}),
        'serie': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N° Serie'}),
        'marca': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Marca'}),
        'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del Equipo'}),
        'servicio': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Servicio'}),
        'responsable': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Jefe de MMTTO y SSGG'}),
        'tecnico1': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre Tecnico'}),
        'tecnico2': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre Tecnico'}),
        'justificacion': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observaciones'}), 
        'fecha': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),  
        }
    