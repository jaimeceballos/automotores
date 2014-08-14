#! /usr/bin/python
# -*- encoding: utf-8 -*-

from django import forms 
from apps.epa.models import *
from django.forms import ModelForm, TimeField
from django.contrib import admin
from django.utils import timezone 
from django.conf import settings
from django.contrib.auth.models import  Group,Permission,User
from django.contrib.admin import widgets
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms.widgets import CheckboxSelectMultiple
from django.core.exceptions import ValidationError
attrs_dict = { 'class': 'required' }

class LoginForm(forms.Form):
	usuario = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'required span9','placeholder':'Usuario'})))
	password = forms.CharField(widget=forms.PasswordInput(attrs=dict({'class':'required span9','placeholder':'Contraseña'}), render_value=False))


class CiudadesForm(forms.ModelForm):
    descripcion = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'required form-control','placeholder':'Descripcion'})),required=True)
    class Meta:
        model = RefCiudades

class DepartamentosForm(forms.ModelForm):
    descripcion = forms.CharField(required=True)
    class Meta:
        model = RefDepartamentos

class ProvinciasForm(forms.ModelForm):
    descripcion = forms.CharField(required=True)
   
    class Meta:
        model = RefProvincia


class PaisesForm(forms.ModelForm):
    descripcion = forms.CharField(required=True)
    class Meta:
		model = RefPaises

class UnidadesForm(forms.ModelForm):
    descripcion = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'required form-control','placeholder':'Descripcion'})),required=True)
    ciudad = forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'required form-control'})), queryset= RefCiudades.objects.all()  )
    class Meta:
        model = UnidadesRegionales
 
class DependenciasForm(forms.ModelForm):
    descripcion = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'required form-control','placeholder':'Descripcion'})),required=True)
    ciudad = forms.ModelChoiceField(widget=forms.Select(dict({'class':'required form-control'})), queryset= RefCiudades.objects.all()  )
    unidades_regionales = forms.ModelChoiceField(widget = forms.Select(dict({'class':'required form-control'})), queryset= UnidadesRegionales.objects.all())

    
    class Meta:
        model = Dependencias     

class TipoVehiculoForm(forms.ModelForm):
    descripcion = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'required form-control','placeholder':'Descripcion'})),required=True)

    class Meta:
        model = TipoVehiculo

class EstadoMovilForm(forms.ModelForm):
    descripcion = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'required form-control','placeholder':'Descripcion'})),required=True)

    class Meta:
        model = EstadoMovil

class RefTrademarkForm(forms.ModelForm):
    descripcion = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'required form-control','placeholder':'Descripcion'})),required=True)    

    class Meta:
        model = RefTrademark

class RefModelosForm(forms.ModelForm):
    marca     = forms.ModelChoiceField(widget = forms.Select(dict({'class':'required form-control'})), queryset= RefTrademark.objects.all())
    descripcion = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'required form-control','placeholder':'Descripcion'})),required=True)    

    class Meta:
        model = RefModelos

class VehiculoForm(forms.ModelForm):
    dominio     = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'required form-control','placeholder':'AAH-113','required':'required'})),required=True)    
    anio        = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control','placeholder':'2014'})))    
    nmotor      = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control','placeholder':'Numero de motor'})))    
    nchasis     = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control','placeholder':'Numero de chasis'})))    
    modelo      = forms.ModelChoiceField(widget = forms.Select(dict({'class':'required form-control'})), queryset= RefModelos.objects.all())
    idmarca     = forms.ModelChoiceField(widget = forms.Select(dict({'class':'required form-control'})), queryset= RefTrademark.objects.all())

    class Meta:
        model = Vehiculo

class MovilForm(forms.ModelForm):
    unidad_regional     = forms.ModelChoiceField(widget = forms.Select(dict({'class':'required form-control'})), queryset= UnidadesRegionales.objects.all())
    dependencia         = forms.ModelChoiceField(widget = forms.Select(dict({'class':'required form-control'})),queryset=Dependencias.objects.all())
    tipo_vehiculo       = forms.ModelChoiceField(widget = forms.Select(dict({'class':'required form-control'})),queryset=TipoVehiculo.objects.all())
    registro_interno    = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'required form-control','placeholder':'Registro Interno','required':'required'})),required=True)    


    class Meta:
        model = Movil

class MovilEstadoForm(forms.ModelForm):
    estado          = forms.ModelChoiceField(widget = forms.Select(dict({'class':'required form-control'})),queryset=EstadoMovil.objects.all())
    observaciones   = forms.CharField(widget = forms.Textarea(dict({'class':'required form-control'})))
    class Meta:
        exclude = ('movil')
        model = MovilEstado