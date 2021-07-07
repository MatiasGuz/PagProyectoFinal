from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import PROTECT

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, null = False)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField(max_length= 411)
    categorias = models.ForeignKey(Categoria, null = True, on_delete= models.PROTECT)
    imagen = models.ImageField(upload_to="productos", null = True)

    def __str__(self):
        return self.nombre