"""boqueria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from paginas import views
from paginas.views import pcontacto, pcontactoenviado #tengo que importar la clase pcontacto de los views
from mercaderia.views import Mercaderia, MercaderiaProveedores


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.base,name="base"),
    path('pproductos/',views.pproductos, name="pproductos"),
    path('pcontacto/',pcontacto.as_view(),name="pcontacto"), #para que lo tome, tengo que ponerle .as_view
    path('pcontactoenviado/', pcontactoenviado.as_view(), name='pcontactoenviado'),
    path('mercaderia/', Mercaderia.as_view(), name='mercaderia'),
    path('proveedores/', MercaderiaProveedores.as_view(), name='proveedores'),
    path('cuentas/', include('django.contrib.auth.urls')),
    path('cuentas/', include('registration.urls')),
]
