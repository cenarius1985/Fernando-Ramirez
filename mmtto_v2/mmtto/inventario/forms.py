from django.forms import ModelForm
from django import forms
from .models import inventario



class InventarioForm(ModelForm):

    class Meta:
        model = inventario
        fields = "__all__"
        widgets = {
        'servicio': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Servicio Clinico o CC'}),
        'clase': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Clase'}),
        'subclase': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Subclase'}),
        'nombre_equipo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Nombre del Equipo'}),
        'marca': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Marca'}),
        'modelo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Modelo'}),
        'serie': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Serie'}),
        'valor': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Valor del Equipo'}),
        'inventario': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N° de Inventario'}),
        'empresa': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre de la Empresa'}),
        'rut': forms.TextInput(attrs={'class':'form-control', 'placeholder':'12345678-9'}),
        'fecha_baja': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Fecha de Baja del Equipo'}),
        'garantia_inicio': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'garantia_final': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'garantia_final': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'fecha':forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'fecha_baja':forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }
