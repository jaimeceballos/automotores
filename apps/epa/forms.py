#! /usr/bin/python
# -*- encoding: utf-8 -*-

from django import forms 
from apps.epa.models import *

attrs_dict = { 'class': 'required' }

class LoginForm(forms.Form):
	usuario = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'required span9','placeholder':'Usuario'})))
	password = forms.CharField(widget=forms.PasswordInput(attrs=dict({'class':'required span9','placeholder':'Contraseña'}), render_value=False))


class CiudadesForm(forms.ModelForm):
    descripcion = forms.CharField(required=True)
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
    descripcion = forms.CharField(required=True)
    ciudad = forms.ModelChoiceField(widget=forms.Select(attrs={'size':'13', 'onchange':'this.form.action=this.form.submit()'}), queryset= RefCiudades.objects.filter(provincia__contains = RefProvincia.objects.filter(descripcion__contains = 'CHUBUT').values('id'))  )
    class Meta:
        model = UnidadesRegionales
 
class DependenciasForm(forms.ModelForm):
    descripcion = forms.CharField(required=True)
    ciudad = forms.ModelChoiceField(widget=forms.Select(attrs={'size':'13', 'onchange':'this.form.action=this.form.submit()'}), queryset= RefCiudades.objects.filter(provincia__contains = RefProvincia.objects.filter(descripcion__contains = 'CHUBUT').values('id'))  )
    unidades_regionales = forms.ModelChoiceField(widget = forms.Select(attrs={'size':'13', 'onchange':'this.form.action=this.form.submit()'}), queryset= UnidadesRegionales.objects.all())

    
    class Meta:
        model = Dependencias     