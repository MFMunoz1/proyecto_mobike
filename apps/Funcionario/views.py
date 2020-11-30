
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import UserPassesTestMixin, AccessMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Funcionario
from .forms import FuncionarioForm

# --IMPORTACIONES DE LA API--
from rest_framework import generics
from .serializers import FuncionarioSerializer

# Create your views here.

class FuncionarioList (ListView):                    
    model = Funcionario
    template_name = 'Funcionario/lista_funcionario.html'

class FuncionarioCreate (CreateView):
    model = Funcionario
    form_class = FuncionarioForm
    template_name = 'Funcionario/funcionario_form.html'
    success_url = reverse_lazy('lista_funcionario')

class FuncionarioUpdate(UpdateView):
    model = Funcionario
    form_class = FuncionarioForm
    template_name = 'Funcionario/funcionario_form.html'
    success_url = reverse_lazy('lista_funcionario')

class FuncionarioDelete(DeleteView):
    model = Funcionario
    template_name = 'Funcionario/borrar_funcionario.html'
    success_url = reverse_lazy('lista_funcionario')


#---API PARA FUNCIONARIO--------------------------------------
class API_objects(generics.ListCreateAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    
class API_objects_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
