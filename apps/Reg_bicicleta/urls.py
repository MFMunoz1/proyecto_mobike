from django.urls import path, include
from . import views
from django.contrib.auth.views import login_required
from .views import SearchResultsView, BuscarBicicletaView

urlpatterns = [

     # LISTA TODAS LAS BICICLETAS
    path('lista_bicicleta', views.Lista_bicicleta.as_view(), name='lista_bicicleta'),

    # FILTRO 1: TRAE SOLO LAS BICICLETAS QUE SEAN DE LA COMUNA DE PROVIDENCIA
    path('lista_bicicleta/comuna/providencia', views.lista_bicicleta_cp, name='lista_providencia'),

    # FILTRO 2: TRAE SOLO LAS BICICLETAS QUE SEAN DE LA COMUNA DE LA REINA 
    path('lista_bicicleta/comuna/la_reina', views.lista_bicicleta_lr, name='lista_la_reina'),

    path('lista_bicicleta/comuna/nunoa', views.lista_bicicleta_cn, name='lista_nunoa'),

    
    # AGREGA UNA BICICLETA
    path('agregar_bicicleta', views.Crear_bicicleta.as_view(), name="agregar_bicicleta"),
    
    # MODIFICA UNA CARRERA 
    path('editar_bicicleta/<int:pk>', login_required(views.Modificar_bicicleta.as_view()), name='editar_bicicleta'),
    
    # ELIMINA UNA CARRERA 
    path('eliminar_bicicleta/<int:pk>', login_required(views.Eliminar_bicicleta.as_view()), name='eliminar_bicicleta'),
    
    #--------------------FILTROS------------------------------------------------------------------------------
    # FILTRO 1: BUSCAR POR COMUNA 
    path('buscar/', BuscarBicicletaView.as_view(), name='buscar_bicicleta'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
]
