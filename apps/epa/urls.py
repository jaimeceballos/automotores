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
)