from django.urls import path
from . import views

app_name = "carrito"

urlpatterns = [
    path("Agregar/<id>/", views.Agregar, name="Agregar"),
    path("Restar/<id>/", views.Restar, name="Restar"),
    path("Eliminar/<id>/", views.EliminarProducto, name="Eliminar"),
    path("Vaciar", views.Vaciar, name="Vaciar"),
]
