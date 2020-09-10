

from django.shortcuts import render, redirect, get_object_or_404
from core.forms import ProductosForm, ClienteForm
from .models import Productos
from .models import Cliente


def index(request):
    return render(request, 'index.html', {'menu': True})


def home(request, plantilla='home.html'):
    return render(request, plantilla)

def about(request, plantilla="about.html"):
    return render(request,plantilla)

def contact(request, plantilla="contact.html"):
    return render(request, plantilla)

def productos(request, plantilla="products.html"):
    productos= list(Productos.objects.all())
    return render(request, plantilla, {'productos':productos })


def cliente(request, plantilla="Cliente.html"):
    cliente=list(Cliente.objects.all())
    return render(request, plantilla, {'cliente':cliente})



#crear productos
def crearproductos(request, template_name="crearproducto.html"):
    if request.method =='POST':
        formProductos=ProductosForm(request.POST or None)
        if formProductos.is_valid():
            formProductos.save()
            return redirect('products')
    else:
        formProductos=ProductosForm()
    return render(request, template_name,{'formProductos':formProductos})

#modificar producto

def modificarproducto(request, pk, template_name="modificarproducto.html"):
    if request.method == "POST":
        Producto =get_object_or_404(Productos, pk=pk)
        formProductos = ProductosForm(request.POST or None, instance=Producto)
        if formProductos.is_valid():
            formProductos.save()
        return redirect("products")
    else:
        Producto = get_object_or_404(Productos, pk=pk)
        formProductos = ProductosForm(request.POST or None, instance=Producto)
    return render(request, template_name, {'formProductos': formProductos})





#eliminar
def eliminarproducto(request, pk, template_name="eliminarproducto.html"):
    if request.method == "POST":
        Producto =get_object_or_404(Productos, pk=pk)
        formProductos = ProductosForm(request.POST or None, instance=Producto)
        if formProductos.is_valid():
            formProductos.save()
        return redirect("products")
    else:
        Producto = get_object_or_404(Productos, pk=pk)
        formProductos = ProductosForm(request.POST or None, instance=Producto)
    return render(request, template_name, {'formProductos': formProductos})

#CLIENTE
def crearcliente(request, template_name="crearcliente.html"):
    if request.method =='POST':
        formCliente=ClienteForm(request.POST or None)
        if formCliente.is_valid():
            formCliente.save()
            return redirect('Cliente')
    else:
        formCliente=ClienteForm()
    return render(request, template_name,{'formCliente':formCliente})
