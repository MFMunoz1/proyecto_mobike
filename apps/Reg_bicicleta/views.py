from django.shortcuts import render
from .models import Bicicleta
from .forms import BicicletaForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q 

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

#-------------------------------FILTROS---------------------------------------------------------
# FILTROS: BUSCAR POR COMUNA Y POR ESTADO
def mantenedor(request):
    lista= Bicicleta.objects.all()
    comuna= request.GET.get('comuna')
    estado= request.GET.get('estado')

    if 'btn-buscarComuna' in request.GET:
       if comuna: 
           lista= Bicicleta.objects.filter(comuna__icontains=comuna)
    elif 'btn-buscarEstado' in request.GET:
        if estado:
            lista= Bicicleta.objects.filter(estado__icontains=estado)
      
    data = {
        'object_list': lista
    }
    return render(request, 'Reg_bicicleta/lista_bicicleta_filtros.html', data)
