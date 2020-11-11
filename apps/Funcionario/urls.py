from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import FuncionarioList, FuncionarioCreate, FuncionarioUpdate , FuncionarioDelete

urlpatterns = [
    path('listar/', FuncionarioList.as_view(), name="lista_funcionario"),

    path('crear/', FuncionarioCreate.as_view(), name="funcionario_form"),
    path('editar/<int:pk>', FuncionarioUpdate.as_view(), name="funcionario_update"),
    path('borrar/<int:pk>', FuncionarioDelete.as_view(), name="funcionario_borrar"),
    
]
