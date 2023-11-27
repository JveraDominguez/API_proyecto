from django.shortcuts import render
from personas.models import automovile
# Create your views here.

def bienvenida(request):
    cantidad_automoviles = automovile.objects.count()
    automoviles = automovile.objects.select_related('propietario').order_by('propietario__nombre', 'propietario__apellido')
    dict_datos = {'cantidad_automoviles': cantidad_automoviles, 'automoviles': automoviles}
    return render(request, 'bienvenida.html', dict_datos)


