from django.db import models

class Tecnico(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} ({self.especialidad})"


class Incidencia(models.Model):
    ESTADOS_CHOICES = [
        ('Abierto', 'Abierto'),
        ('En Proceso', 'En Proceso'),
        ('Cerrado', 'Cerrado'),
    ]
    
    PRIORIDAD_CHOICES = [
        ('Baja', 'Baja'),
        ('Media', 'Media'),
        ('Alta', 'Alta'),
    ]

    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS_CHOICES, default='Abierto')
    prioridad = models.CharField(max_length=20, choices=PRIORIDAD_CHOICES, default='Media')
    
    # Relación con el técnico asignado (ForeignKey)
    tecnico = models.ForeignKey(Tecnico, on_delete=models.SET_NULL, null=True, blank=True, related_name='incidencias')

    def __str__(self):
        return f"[{self.estado}] {self.titulo} - Prioridad: {self.prioridad}"