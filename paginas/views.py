from django.shortcuts import render
from .forms import Contactoform
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView #importo para que lo herede la vista de pcontacto basado en clase
from django.urls import reverse_lazy
from .models import Page
from django.urls import reverse
# Create your views here.
def base(request):
    return render(request,"paginas/base.html")


def pproductos(request):
    return render(request,"paginas/pproductos.html")

'''
def pcontacto(request):
    #form = Contactoform()
    model = Page
    form_class = Contactoform
    if request.method == "POST":
        contacto_form = Contactoform(request.POST)
        if contacto_form.is_valid():
            messages.success(request,"formulario cagado con exito")
            # return HttpResponseRedirect('gracias')
    else:
        contacto_form = Contactoform()
    return render(request,"paginas/pcontacto.html",{'contacto_form' : contacto_form})   
'''
class pcontacto(CreateView): #el cambio de vista basada en función a vista basada de clase
    model = Page
    form_class = Contactoform
    #success_url = reverse_lazy('pcontacto')
    
    def get_success_url(self):
        return reverse_lazy('pcontactoenviado') + '?ok'

class pcontactoenviado(CreateView):
    model = Page
    form_class = Contactoform
    template_name_suffix = '_formsubmit'

def pproductos(request):
    return render(request,"paginas/pproductos.html")        