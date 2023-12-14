from django import forms
from django.forms import widgets

from .models import Persona, automovile, fabricante

class CrearPersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'cedula']

class CrearAutomovilForm(forms.ModelForm):
    propietario = forms.ModelChoiceField(queryset=Persona.objects.all())
    fabricante = forms.ModelChoiceField(queryset=fabricante.objects.all())

    class Meta:
        model = automovile
        fields = ['marca_auto', 'color_auto', 'placa_auto', 'propietario', 'fabricante', 'fecha_compra']

        widgets = {
            'fecha_compra': forms.DateInput(attrs={'type': 'date'}),
        }
