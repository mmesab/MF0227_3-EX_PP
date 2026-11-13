# incidencias/views.py
from django.shortcuts import render, redirect
from .models import Incidencia
from .forms import IncidenciaForm

def lista_incidencias(request):
    incidencias = Incidencia.objects.all().order_by('-fecha_creacion')
    return render(request, 'incidencias/lista_incidencias.html', {'incidencias': incidencias})

def crear_incidencia(request):
    if request.method == 'POST':
        form = IncidenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_incidencias')
    else:
        form = IncidenciaForm()
    return render(request, 'incidencias/crear_incidencia.html', {'form': form})