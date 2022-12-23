from django.db import models

# Create your models here.
#se podria cambiar el nombre de este modelo, modelo para el formulario
class Page(models.Model):
    nombre = models.TextField(verbose_name="nombre")
    apellido = models.TextField(verbose_name="apellido")
    email = models.EmailField(verbose_name="email")
    mensaje = models.TextField(verbose_name="mensaje")
    
    
    class Meta:
        verbose_name = "contacto"

    def __str__(self):
        return self.title

