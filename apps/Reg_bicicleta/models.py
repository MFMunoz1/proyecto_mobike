from django.db import models

# Create your models here.
class Bicicleta(models.Model):
    comuna = models.CharField(max_length=40)
    ubicacion = models.CharField(max_length=50)
    estado = models.CharField(max_length=40)

    def __str__(self):
        return self.comuna
