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
  url(r'^estadosmovil/$',  estadosmovil, name='estadosmovil'),
  url(r'^estadosmovil/(?P<id_estado>\d+)/$',  estadomovil, name='estadomovil'),
  url(r'^moviles/$',  moviles, name='moviles'),
  url(r'^moviles/nuevo/$',  nuevo, name='nuevo'),
)