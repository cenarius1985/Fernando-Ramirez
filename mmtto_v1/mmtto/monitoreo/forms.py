from django.forms import ModelForm
from django import forms
from .models import monitoreo

class MonitoreoForm(ModelForm):

    class Meta:
        model = monitoreo
        fields = "__all__"
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
    