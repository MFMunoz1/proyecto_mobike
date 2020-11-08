from django.shortcuts import render
from .models import Bicicleta
from .forms import BicicletaForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

class Lista_bicicleta(ListView):
    model = Bicicleta
    template_name = 'Reg_bicicleta/lista_bicicleta.html'

# LISTA BICICLETA QUE SEAN DE LA COMUNA DE PROVIDENCIA 
def lista_bicicleta_cp(request):
     providencia = Bicicleta.objects.filter(comuna = 'providencia')
     return render(request, "Reg_bicicleta/lista_filtro_comuna.html", {'comuna':providencia})

# LISTA BICICLETA QUE SEAN DE LA COMUNA DE LA REINA
def lista_bicicleta_lr(request):
     la_reina = Bicicleta.objects.filter(comuna = 'la_reina')
     return render(request, "Reg_bicicleta/lista_filtro_comuna.html", {'comuna':la_reina})

def lista_bicicleta_cn(request):
     nunoa = Bicicleta.objects.filter(comuna = 'nunoa')
     return render(request, "Reg_bicicleta/lista_filtro_comuna.html", {'comuna':nunoa})


class Crear_bicicleta(CreateView): 
    model = Bicicleta 
    form_class = BicicletaForm 
    template_name = 'Reg_bicicleta/bicicleta_form.html' 
    success_url = reverse_lazy("lista_bicicleta")
    
class Modificar_bicicleta(UpdateView):
    model = Bicicleta
    form_class = BicicletaForm
    template_name = 'Reg_bicicleta/bicicleta_form.html'
    success_url = reverse_lazy('lista_bicicleta')
    
class Eliminar_bicicleta(DeleteView):
    model = Bicicleta
    template_name = 'Reg_bicicleta/elimina_bicicleta.html'
    success_url = reverse_lazy('lista_bicicleta')

