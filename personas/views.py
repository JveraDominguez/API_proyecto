
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CrearAutomovilForm, CrearPersonaForm
from .models import Persona, automovile


# Create your views here.
# views.py

def ver_persona(request, persona_id):
    persona = get_object_or_404(Persona, pk=persona_id)
    automoviles = persona.automoviles.all()
    datos = {'persona': persona, 'automoviles': automoviles}
    return render(request, 'ver_auto.html', datos)

def eliminar_persona(request, persona_id):
    persona = get_object_or_404(Persona, pk=persona_id)

    # Obtenemos todos los autos asociados a esta persona
    autos_asociados = automovile.objects.filter(propietario=persona)

    if request.method == 'POST':
        # Eliminamos la persona y todos sus autos asociados
        persona.delete()
        autos_asociados.delete()

        return redirect('inicio')  # Reemplaza 'bienvenida' con el nombre de tu URL de bienvenida

    return render(request, 'eliminar_persona.html', {'persona': persona, 'autos_asociados': autos_asociados})


def crear_persona(request):
    if request.method == 'POST':
        form = CrearPersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')  # Reemplaza con la URL correcta
    else:
        form = CrearPersonaForm()

    return render(request, 'crear_persona.html', {'form': form})


def crear_automovil(request):
    if request.method == 'POST':
        form = CrearAutomovilForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')  # Reemplaza con la URL correcta
    else:
        form = CrearAutomovilForm()

    return render(request, 'crear_automovil.html', {'form': form})

def editar_persona(request, persona_id):
    persona = get_object_or_404(Persona, pk=persona_id)

    if request.method == 'POST':
        form_persona = CrearPersonaForm(request.POST, instance=persona)
        if form_persona.is_valid():
            form_persona.save()
            return redirect('inicio')

    else:
        form_persona = CrearPersonaForm(instance=persona)

    return render(request, 'editar_persona.html', {'form_persona': form_persona, 'persona': persona})


def editar_automovil(request, automovil_id):
    automovil = get_object_or_404(automovile, pk=automovil_id)

    if request.method == 'POST':
        form_automovil = CrearAutomovilForm(request.POST, instance=automovil)
        if form_automovil.is_valid():
            form_automovil.save()
            return redirect('inicio')

    else:
        form_automovil = CrearAutomovilForm(instance=automovil)

    return render(request, 'editar_automovil.html', {'form_automovil': form_automovil, 'automovil': automovil})
