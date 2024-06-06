from django.db import models

# Create your models here.


class Medicamentos(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)


class Tratamientos(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    medicamentos = models.ManyToManyField(Medicamentos, blank=True, null=True, related_name='trat_medicamento')


class Enfermedades(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    tratamientos = models.ManyToManyField(Tratamientos, blank=True, null=True, related_name='enfermedad_tratamiento')
