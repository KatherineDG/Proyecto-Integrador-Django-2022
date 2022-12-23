from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Productos, Proveedores
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(staff_member_required, name='dispatch')
class Mercaderia(ListView):
    template_name = 'productos_list.html'
    model = Productos

class MercaderiaProveedores(ListView):
    template_name = 'proveedores_list.html'
    model = Proveedores

