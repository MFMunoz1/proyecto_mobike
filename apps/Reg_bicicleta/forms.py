from django import forms
from .models import Bicicleta 

class BicicletaForm(forms.ModelForm): 
    class Meta:  
        model = Bicicleta
        fields = ['comuna', 'ubicacion', 'estado'] 

        labels = {
            'comuna': 'Comuna',
            'ubicacion': 'Ubicacion',
            'estado': 'Estado', 

        }
        widgets = {
            'comuna': forms.TextInput(attrs={'class': 'form-control'}), 
            'ubicacion': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
           
        }
