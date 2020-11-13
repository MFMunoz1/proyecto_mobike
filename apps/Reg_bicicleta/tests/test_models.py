from django.test import TestCase
from django.template.defaultfilters import slugify
from apps.Reg_bicicleta.models import Bicicleta
from apps.Reg_bicicleta.forms import BicicletaForm

class CarreraTestCase(TestCase):
    def setUp(self):
        Bicicleta.objects.create(comuna="providencia", ubicacion="direccion 1", estado="alta")
        Bicicleta.objects.create(comuna="nunoa", ubicacion="direccion 2", estado="baja")

# SE PRUEBA SI EL VALOR DEL OBJETO QUE TRAJO DE LA BDD (GET) COINCIDE CON EL VALOR QUE 
# SE PRECARGÓ ANTES (EN EL SETUP)
    def test_ingresar_bicicletas(self):
        """Las carreras se registran correctamente en la BD"""
        bicicleta_1 = Bicicleta.objects.get(comuna="providencia") # TRAE DETERMINADOS OBJETOS DE LA BDD
        bicicleta_2 = Bicicleta.objects.get(comuna="nunoa")
        self.assertEqual(bicicleta_1.estado, "alta") #--> HACE LA COMPARACIÓN 
        self.assertEqual(bicicleta_2.estado, "baja")