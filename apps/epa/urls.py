#! /usr/bin/python
# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, include, url
from views import *

urlpatterns=patterns( '',  
  url(r'^$',  home, name='home'),
  url(r'^unidades/$',  unidades, name='unidades'),
  url(r'^unidades/(?P<id_unidad>\d+)/$',  unidad, name='unidad'),
  url(r'^agregaciudad/$',  agregaciudad, name='agregaciudad'),
  url(r'^dependencias/$',  dependencias, name='dependencias'),
  url(r'^dependencias/(?P<id_depe>\d+)/$',  dependencia, name='dependencia'),
  url(r'^tiposvehiculos/$',  tiposvehiculos, name='tiposvehiculos'),
  url(r'^tiposvehiculos/(?P<id_tipo>\d+)/$',  tipovehiculo, name='tipovehiculo'),
  url(r'^marca/$',  marcas, name='marcas'),
  url(r'^marca/(?P<id_marca>\d+)/$',  marca, name='marca'),
  url(r'^modelo/$',  modelos, name='modelos'),
  url(r'^modelo/(?P<id_modelo>\d+)/$',  modelo, name='modelo'),
  url(r'^estadosmovil/$',  estadosmovil, name='estadosmovil'),
  url(r'^estadosmovil/(?P<id_estado>\d+)/$',  estadomovil, name='estadomovil'),
  url(r'^moviles/$',  moviles, name='moviles'),
  url(r'^moviles/nuevo/$',  nuevo, name='nuevo'),
  url(r'^moviles/modificar/(?P<id_movil>\d+)/$',  modifica_movil, name='modifica_movil'),
  url(r'^obtener_dependencias/(?P<id_unidad>\d+)/$',  obtener_dependencias, name='obtener_dependencias'),
  url(r'^moviles/listar/$',  listar, name='listar'),
  url(r'^moviles/cargarestado/(?P<id_movil>\d+)/$',  cargar_estado, name='cargar_estado'),
  url(r'^moviles/estado/$',  estado, name='estado'),
)