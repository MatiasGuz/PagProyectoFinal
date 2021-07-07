from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home , name="Home"),
    path('AcercaDe', views.AcercaDe, name = "AcercaDe"),
    path('contacto', views.contacto, name = "contacto"),
    path('agregar', views.Agregar, name= "Agregar_Producto"),
    path('Lista', views.Lista, name= "Lista_Producto"),
    path('Editar/<id>/', views.Editar, name = "Editar_Producto"),
    path('Eliminar/<id>/', views.Eliminar, name = "Eliminar_Producto"),
    path('Registrarse', views.Registro , name = "Registro"),
    path('Filtro_de_categorias/<id>/', views.Filtro_Categorias, name="filtro_de_categorias"),
    path('VerProducto/<id>/', views.VerProducto, name = "VerProducto"),
    path('FiltroCategorias/<id>/', views.Filtro_Categorias, name = "FiltroCategorias"),
    path("Carrito", views.Carrito, name="Carrito"),
]