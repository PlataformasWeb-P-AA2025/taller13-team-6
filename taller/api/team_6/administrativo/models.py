from django.db import models


# Create your models here.
class Edificio(models.Model):
    TIPO_CHOICES = [
        ('RESIDENCIAL', 'Residencial'),
        ('COMERCIAL', 'Comercial'),
    ]

    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    tipo = models.CharField(max_length=11, choices=TIPO_CHOICES)

    def __str__(self):
        return self.nombre
    
class Departamento(models.Model):
    nombre_propietario = models.CharField(max_length=100)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    num_cuartos = models.IntegerField()
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE,
            related_name="edificio_departamentos")

    def __str__(self):
        return f"{self.costo} - {self.edificio.nombre}"