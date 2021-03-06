from django.shortcuts import render, redirect, get_object_or_404
from .models import Bicicleta
from .forms import BicicletaForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q 

#--IMPORTACIONES PARA LA API ---------------------
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BicicletaSerializer
from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 



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


# ----FUNCIONES API --------------------------
@api_view(['GET', 'POST'])
def bicicleta_collection(request):
    # SE LISTAN TODOS LOS OBJETOS DE LA COLECCIÓN 
    if request.method == 'GET':
        bicicletas = Bicicleta.objects.all()
        serializer = BicicletaSerializer(bicicletas, many=True)
        return Response(serializer.data)
    
    # SE AGREGA UN OBJETO A LA COLECCIÓN 
    elif request.method == 'POST':
        serializer = BicicletaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

@api_view(['GET', 'PUT', 'DELETE'])
def bicicleta_element(request, pk):
    bicicleta = get_object_or_404(Bicicleta, id=pk)
    # SE LISTA UN SOLO OBJETO DE LA COLECCIÓN
    if request.method == 'GET':
        serializer = BicicletaSerializer(bicicleta)
        return Response(serializer.data)
    
    # SE ELIMINA UN OBJETO DE LA COLECCIÓN
    elif request.method == 'DELETE':
        bicicleta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # SE MODIFICA UN OBJETO DE LA COLECCIÓN
    elif request.method == 'PUT': 
        bicicleta_new = JSONParser().parse(request) 
        serializer = BicicletaSerializer(bicicleta, data=bicicleta_new) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    
    
