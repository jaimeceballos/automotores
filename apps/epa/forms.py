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