from django.test import TestCase
from django.test import Client

# SE PRUEBA QUE EL LOCALHOST BASE CARGUE CORRECTAMENTE 
class ViewsTestCase(TestCase):
    def test_index_loads_properly(self): #---> prueba si carga correctamente la página de inicio
        response = self.client.get('http://localhost:8000/') #--> hagamos cuenta que el cliente quiere obtener este requerimiento
        self.assertEqual(response.status_code, 200) #--> compara con el 200 que significa que es el resultado esperado, o sea, que todo funciona perfecto
  
