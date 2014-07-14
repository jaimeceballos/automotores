#! /usr/bin/python
# -*- encoding: utf-8 -*-

from django import forms 

attrs_dict = { 'class': 'required' }

class LoginForm(forms.Form):
	usuario = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'required span9','placeholder':'Usuario'})))
	password = forms.CharField(widget=forms.PasswordInput(attrs=dict({'class':'required span9','placeholder':'Contraseña'}), render_value=False))
