from django.db import models

# Create your models here.

class Project(models.Model):
    title=models.CharField(max_length=200)
    description= models.CharField(max_length=200)
    user = models.CharField(max_length=20)
    user_mod = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Productos(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion=models.CharField(max_length=200)
    precio=models.IntegerField()
    unidades=models.IntegerField()
    user = models.CharField(max_length=20)
    user_mod = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tr_Productos"
        verbose_name ="Producto"
        verbose_name_plural ="Productos"
        ordering = ['-created']

    def __str__(self):
        return self.nombre



class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    telefono = models.IntegerField()
    Productos = models.ManyToManyField(Productos)
    user = models.CharField(max_length=20)
    user_mod = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tr_Cliente"
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['-created']

    def __str__(self):
            return self.nombre


class Producto_Cliente(models.Model):
    Producto= models.ForeignKey(Productos, on_delete=models.CASCADE)
    Cliente= models.ForeignKey(Cliente, on_delete=models.CASCADE)