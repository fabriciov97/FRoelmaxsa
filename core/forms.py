from django import forms

from core.models import Productos
from core.models import Cliente


class ProductosForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['nombre', 'descripcion','precio','unidades']



class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'direccion','telefono']