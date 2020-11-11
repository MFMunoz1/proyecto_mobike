from django.db import models

# Create your models here.
RAMA_EJECUTIVA = (
    ('Gerencia', 'Gerencia'),
    ('Administracion', 'Administracion'),
    ('Informatica', 'Informatica'),
    ('Alcaldia', 'Alcaldia'),
)

class Funcionario (models.Model):
    fotografia = models.ImageField(upload_to='funcionarios')
    rut = models.CharField(max_length=15)
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=70,blank=True, null= True, unique= True)
    rama_ejecutiva = models.CharField(max_length=50, choices=RAMA_EJECUTIVA)

    def __str__(self):
        return str(self.fotografia)

