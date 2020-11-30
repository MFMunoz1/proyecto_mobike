from rest_framework import serializers
from .models import Bicicleta

class BicicletaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bicicleta
        fields = ('id', 'comuna', 'ubicacion', 'estado')
