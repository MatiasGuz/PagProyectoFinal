from django.contrib.auth.forms import UserCreationForm
from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse, request
from .models import Producto, Categoria
from .forms import AgregarForm, RegistroForm
from django.contrib  import messages
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.

def Home(request):
    
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, "plantillas/Home.html", data)

def AcercaDe(request):
    return render(request, "plantillas/AcercaDe.html")

def contacto(request):
    return render(request, "plantillas/contacto.html")
@permission_required('ProyectoFinal.add_producto')
def Agregar(request):
    data = {
        'form' : AgregarForm()
    }

    if request.method == 'POST':
        formulario = AgregarForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Agregado correctamente")
        else:
            data["form"] = formulario

    return render(request, "producto/agregar.html", data)
@permission_required('ProyectoFinal.view_producto')
def Lista(request):
    productos = Producto.objects.all()

    data = {
        'productos' : productos,
    }
    return render(request, 'producto/lista.html', data)
@permission_required('ProyectoFinal.change_producto')
def Editar(request, id):

    producto = get_object_or_404(Producto, id=id)

    data = {
        'form' : AgregarForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = AgregarForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente")
            return redirect(to="Lista_Producto")
        else:
            data["form"] = formulario

    return render(request, 'producto/editar.html', data)
@permission_required('ProyectoFinal.delete_producto')
def Eliminar(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to = "Lista_Producto")

def Registro(request):

    data = {
        'form' : RegistroForm()
    }

    if request.method == 'POST':
        formulario = RegistroForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to='Home')
        data["form"] = formulario


    return render(request, 'registration/register.html', data)

def Filtro_Categorias(request, id):
    categoria = get_object_or_404(Categoria, id = id)
    producto = Producto.objects.all()
    producto = producto.filter(categoria = categoria)
    return render(request, 'plantillas/Home.html', {
        "lista_productos" : producto,
        "lista_categoria" : Categoria.objects.all(),
        "categoria_seleccionada" : categoria
    })

def VerProducto(request, id):
    producto = get_object_or_404(Producto, id = id)
    return render(request, 'producto/VerProducto.html',{
        "producto" : producto
    })

def Carrito(request):
    return render(request, 'plantillas/carrito.html')

