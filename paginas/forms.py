from django import forms 
from django.core import validators
from django.forms import ValidationError
from .models import Page

class Contactoform(forms.ModelForm):

    class Meta:
        model = Page
        fields = ['nombre', 'apellido', 'email', 'mensaje']
        widgets = {
            'nombre' : forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Juan', 'size':'32'}),
            'apellido' : forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Garcia', 'size':'32'}),
            'email' : forms.EmailInput(attrs = {'class':'form-control', 'placeholder':'ejemplo@ejemplo.com', 'size':'35'}),
            'mensaje' : forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Escriba aqui...', 'cols': 36, 'rows': 10})
        }
        labels = {
            'nombre':'nombre', 'apellido':'apellido', 'email':'email', 'mensaje':'mensaje'
        }
        

    
    #VALIDACIONES 

    #metodo para validar algun atributo, def clean_nombreAtributo(self)
    def clean_nombre(self):
        ''' Validar que nombre sea correcto
        '''
        #cleaned_data: cuando se envia la info a traves del form, aquella llegará a django y se guarda en una variable, es un diccionario y ahi se guardaria, y con el .get(clavereferencia) podemos extraerlo
        nombre = self.cleaned_data.get('nombre')
        #print(nombre.isalpha())
        if nombre.isalpha() == False:
            raise forms.ValidationError("Su nombre no deberia contener simbolos o números.")
        else:
            return nombre
        
    def clean_apellido(self):
        ''' Validar que nombre sea correcto
        '''
        #cleaned_data: cuando se envia la info a traves del form, aquella llegará a django y se guarda en una variable, es un diccionario y ahi se guardaria, y con el .get(clavereferencia) podemos extraerlo
        apellido = self.cleaned_data.get('apellido')
        #print(nombre.isalpha())
        if apellido.isalpha() == False:
            raise forms.ValidationError("Su apellido no deberia contener simbolos o números.")
        else:
            return apellido 
        
    def clean_email(self):
        #cleaned_data: cuando se envia la info a traves del form, aquella llegará a django y se guarda en unavariable, es un diccionario ahi se guardaria, y con el .get(clavereferencia) podemos extraerlo
        email = self.cleaned_data.get('email')
        if ((email.rfind('@') and email.rfind('.')) and ((email[len(email)-7]) == ".") and ((email[len(email)-3]) == ".") or ((email[len(email)-4]) == ".") ):
            return email
        else:
            #si no es válido el email, lanzamos una excepcion
            raise forms.ValidationError("Correo electrónico no válido.")

'''
class Contactoform(forms.Form):
    nombre = forms.CharField(label= "nombre ")
    apellido = forms.CharField(label= "apellido ")
    email = forms.EmailField(label="email ")
    comentario =forms.CharField(widget=forms.Textarea(attrs={'size': '30'}))
'''

    