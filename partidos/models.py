from django.db import models

# Create your models here.

from django.db import models

class Partido(models.Model):
    nombre = models.CharField(max_length=100)
    lider = models.CharField(max_length=100)
    fecha_fundacion = models.DateField()

    def __str__(self):
        return self.nombre
