from django import forms
from .models import Persona, automovile, fabricante

class CrearPersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido']

class CrearAutomovilForm(forms.ModelForm):
    propietario = forms.ModelChoiceField(queryset=Persona.objects.all())
    fabricante = forms.ModelChoiceField(queryset=fabricante.objects.all())

    class Meta:
        model = automovile
        fields = ['marca_auto', 'color_auto', 'placa_auto', 'propietario', 'fabricante']
