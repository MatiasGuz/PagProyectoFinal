from ProyectoFinal.models import Producto
from django.shortcuts import render, redirect
from .carrito import Carrito
# Create your views here.

def Agregar(request, id):
    carrito = Carrito(request)
    producto = Producto.objects.get( id = id)
    carrito.AgregarCarrito(producto = producto)
    return redirect("Home")

def EliminarProducto(request, id):
    carrito = Carrito(request)
    producto = Producto.objects.get( id = id)
    carrito.Eliminar(producto = producto)
    return redirect("Home")

def Restar(request, id):
    carrito = Carrito(request)
    producto = Producto.objects.get( id = id)
    carrito.RestarUnidad(producto = producto)
    return redirect("Home")

def Vaciar(request):
    carrito = Carrito(request)
    carrito.VaciarCarrito()
    return redirect("Home")