from .models import Funcionario
from django import forms

class FuncionarioForm(forms.ModelForm):
    

    class Meta:
        model = Funcionario
        fields = (
            'fotografia',
            'rut',
            'nombre',
            'email',
            'rama_ejecutiva'
        )
        labels = {
            'fotografia':'Fotografia',
            'rut':'RUN',
            'nombre':'Nombre',
            'email':'Correo electronico',
            'rama_ejecutiva':'Rama Ejecutiva'
        }
        widgets = {
            'rut':forms.TextInput(attrs={'class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'rama_ejecutiva':forms.Select(choices="RAMA_EJECUTIVA", attrs={'class':'form-control'}),
        }
