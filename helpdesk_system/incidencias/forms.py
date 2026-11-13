# incidencias/forms.py
from django import forms
from .models import Incidencia

class IncidenciaForm(forms.ModelForm):
    class Meta:
        model = Incidencia
        fields = ['titulo', 'descripcion', 'prioridad', 'tecnico']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de la incidencia'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Describe el problema...'}),
            'prioridad': forms.Select(attrs={'class': 'form-select'}),
            'tecnico': forms.Select(attrs={'class': 'form-select'}),
        }