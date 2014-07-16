from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponseRedirect, HttpResponse, Http404
import datetime
from django.conf import settings
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from datetime import datetime
from django.forms.forms import NON_FIELD_ERRORS
from apps.epa.forms import *
from django.views.decorators.cache import cache_control

def login(request):
	form = LoginForm()

	if request.method =='POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			usuario = form.data['usuario']
			password = form.data['password']
			print auth.authenticate(username=usuario,password=password)
			user = auth.authenticate(username=usuario,password=password)
			if user is not None and user.is_active:

				auth.login(request,user)
				return HttpResponseRedirect(reverse('home'))
	values={
		'form':form,
	}
	return render_to_response('accounts/login.html',values, context_instance = RequestContext(request))

def home(request):

	values={
		
	}
	return render_to_response('base.html',values, context_instance = RequestContext(request))	

def logout(request):
	auth.logout(request)

	return HttpResponseRedirect(reverse('login'))

def unidades(request):
	form = UnidadesForm()
	ciudades = CiudadesForm()
	unidades = UnidadesRegionales.objects.all()
	ciudades.fields['pais'].initial = RefPaises.objects.get(descripcion__contains='ARGENTINA')
	ciudades.fields['provincia'].initial = RefProvincia.objects.get(descripcion__contains='CHUBUT')
	if request.method == 'POST':
		form = UnidadesForm(request.POST)
		if form.is_valid():
			unidad = UnidadesRegionales()
			unidad.ciudad = form.cleaned_data['ciudad']
			unidad.descripcion = form.cleaned_data['descripcion']
			unidad.save()
			form=UnidadesForm()
	values={
		'form':form,
		'ciudades':ciudades,
		'unidades':unidades,
	}
	return render_to_response('referencias/unidades.html',values, context_instance = RequestContext(request))	
def unidad(request,id_unidad):
	unidad = UnidadesRegionales.objects.get(id=id_unidad)
	form = UnidadesForm(instance=unidad)
	ciudades = CiudadesForm()
	unidades = UnidadesRegionales.objects.all()
	ciudades.fields['pais'].initial = RefPaises.objects.get(descripcion__contains='ARGENTINA')
	ciudades.fields['provincia'].initial = RefProvincia.objects.get(descripcion__contains='CHUBUT')
	if request.method == 'POST':
		form = UnidadesForm(request.POST)
		if form.is_valid():
			unidad.ciudad = form.cleaned_data['ciudad']
			unidad.descripcion = form.cleaned_data['descripcion']
			unidad.save()
			return HttpResponseRedirect(reverse('unidades'))
	values={
		'unidad':unidad,
		'form':form,
		'ciudades':ciudades,
		'unidades':unidades,
	}
	return render_to_response('referencias/unidades.html',values, context_instance = RequestContext(request))	

def agregaciudad(request):
	formulario = ""
	if request.method == 'POST':
		descripcion = request.POST['descripcion']
		if not descripcion == '':
			ciudad 				= RefCiudades()
			ciudad.pais 		= RefPaises.objects.get(descripcion__contains='ARGENTINA')
			ciudad.provincia 	= RefProvincia.objects.get(descripcion__contains='CHUBUT')
			ciudad.descripcion 	= descripcion
			ciudad.save()
			formulario = request.POST['formulario']
	return HttpResponseRedirect(reverse(formulario))

def dependencias(request):
	form = DependenciasForm()
	ciudades = CiudadesForm()
	dependencias = Dependencias.objects.all()
	ciudades.fields['pais'].initial = RefPaises.objects.get(descripcion__contains='ARGENTINA')
	ciudades.fields['provincia'].initial = RefProvincia.objects.get(descripcion__contains='CHUBUT')
	if request.method == 'POST':
		form = DependenciasForm(request.POST)
		if form.is_valid():
			dependencia = Dependencias()
			dependencia.ciudad = form.cleaned_data['ciudad']
			dependencia.unidades_regionales = form.cleaned_data['unidades_regionales']
			dependencia.descripcion = form.cleaned_data['descripcion']
			dependencia.save()
			form = DependenciasForm()
	values={
		'form':form,
		'ciudades':ciudades,
		'dependencias':dependencias,
	}
	return render_to_response('referencias/dependencias.html',values, context_instance = RequestContext(request))

def dependencia(request,id_depe):
	dependencia = Dependencias.objects.get(id=id_depe)
	form = DependenciasForm(instance=dependencia)
	ciudades = CiudadesForm()
	dependencias = Dependencias.objects.all()
	ciudades.fields['pais'].initial = RefPaises.objects.get(descripcion__contains='ARGENTINA')
	ciudades.fields['provincia'].initial = RefProvincia.objects.get(descripcion__contains='CHUBUT')
	if request.method == 'POST':
		form = DependenciasForm(request.POST)
		if form.is_valid():
			dependencia.ciudad = form.cleaned_data['ciudad']
			dependencia.unidades_regionales = form.cleaned_data['unidades_regionales']
			dependencia.descripcion = form.cleaned_data['descripcion']
			dependencia.save()
			return HttpResponseRedirect(reverse('dependencias'))
	values={
		'dependencia':dependencia,
		'form':form,
		'ciudades':ciudades,
		'dependencias':dependencias,
	}
	return render_to_response('referencias/dependencias.html',values, context_instance = RequestContext(request))