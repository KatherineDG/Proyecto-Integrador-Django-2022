from django.db import models

class Proveedores(models.Model):
    id = models.AutoField(primary_key= True)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    dia_entrega = models.TextField(blank=False,null=False)

    class Meta:
        verbose_name = "proveedor"
        verbose_name_plural = "proveedores"
        ordering = ['nombre']

    def _str_(self):
        return self.nombre

class Productos (models.Model):
    id = models.AutoField(primary_key= True)
    articulo = models.CharField(max_length=50,blank=False,null=False)
    marca = models.CharField(max_length=50,blank= False, null=False)
    precio = models.IntegerField(blank=False,null=False)
    proveedor_id = models.ManyToManyField(Proveedores)
    
    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"
        ordering =['articulo']

    def _str_(self):
        return self.articulo