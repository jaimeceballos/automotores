#! /usr/bin/python
# -*- encoding: utf-8 -*-|

from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import Group,Permission,User
from django.db.models import signals

class RefPaises(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField("Seleccione Pais :", unique=True, max_length=45L )
    

    def __unicode__(self):
      return  u'%s' % (self.descripcion)  
      self.descripcion = self.descripcion.upper()
     
    
    class Meta: 
        ordering = ["descripcion"]
        db_table = 'ref_paises'

    def save(self, force_insert=False, force_update=False):
        self.descripcion = self.descripcion.upper()
        super(RefPaises, self).save(force_insert, force_update)        


class RefProvincia(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField("Ingrese Provincia :", max_length=45L)
    pais = models.ForeignKey(RefPaises,on_delete=models.PROTECT)
    

    def __unicode__(self):
        return  u'%s' % (self.descripcion)
        self.descripcion = self.descripcion.upper()

    
    def save(self, force_insert=False, force_update=False):
        self.descripcion = self.descripcion.upper()
        super(RefProvincia, self).save(force_insert, force_update)

    class Meta:
        unique_together=('descripcion','pais',)
        db_table = 'ref_provincia'
        ordering = ["descripcion"]
     
class RefDepartamentos(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField("Ingrese Departamento :", unique=True, max_length=45L)
    provincia = models.ForeignKey(RefProvincia, on_delete=models.PROTECT)
       
    def __unicode__(self):
        return  u'%s' %  (self.descripcion)
        self.descripcion = self.descripcion.upper()
        
    
    def save(self, force_insert=False, force_update=False):
        self.descripcion = self.descripcion.upper()
        super(RefDepartamentos, self).save(force_insert, force_update)

    class Meta:
        #unique_together=('descripcion','provincia',)
        ordering = ["descripcion"]
        db_table = 'ref_departamentos'
        
class RefCiudades(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=80L)
    departamento = models.ForeignKey('RefDepartamentos',blank=True, null=True, on_delete=models.PROTECT)
    provincia = models.ForeignKey('RefProvincia', blank=True,  null=True, on_delete=models.PROTECT)
    pais = models.ForeignKey('RefPaises', on_delete=models.PROTECT)
    
    def __unicode__(self):
        return  u'%s' %  (self.descripcion)
        self.descripcion = self.descripcion.upper()

    def save(self, force_insert=False, force_update=False):
        self.descripcion = self.descripcion.upper()
        super(RefCiudades, self).save(force_insert, force_update)

    class Meta:
        unique_together = ('pais','provincia','departamento','descripcion',)
        ordering = ["descripcion"]
        db_table = 'ref_ciudades'


class UnidadesRegionales(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=80L)
    ciudad = models.ForeignKey('RefCiudades',on_delete=models.PROTECT)
     
    def __unicode__(self):
        return u'%s' %  (self.descripcion)
        self.descripcion = self.descripcion.upper()
         
 
    def save(self, force_insert=False, force_update=False):
        self.descripcion = self.descripcion.upper()
        super(UnidadesRegionales, self).save(force_insert, force_update)
 
    class Meta:
        unique_together = ('descripcion','ciudad')
        ordering = ["descripcion"]
        db_table = 'unidades_regionales'

class Dependencias(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=80)
    unidades_regionales = models.ForeignKey('UnidadesRegionales', related_name="unidades", on_delete=models.PROTECT)
    ciudad = models.ForeignKey('RefCiudades',on_delete=models.PROTECT)
   
 
    def __unicode__(self):
        return u'%s' % (self.descripcion)
        self.descripcion = self.descripcion.upper()
 
    def save(self, force_insert=False, force_update= False):
        self.descripcion = self.descripcion.upper()
        super(Dependencias, self).save(force_insert,force_update)
 
    class Meta:
        unique_together = ('descripcion','unidades_regionales','ciudad')
        ordering = ["descripcion"]
        db_table = 'dependencias'

class TipoVehiculo(models.Model):
    descripcion = models.CharField(max_length=50,unique=True)

    def __unicode__(self):
        return u'%s' % (self.descripcion)
        self.descripcion = self.descripcion.upper()

    def save(self, force_insert=False,force_update=False):
        self.descripcion = self.descripcion.upper()
        super(TipoVehiculo, self).save(force_insert,force_update)

    class Meta:
        db_table = 'tipo_vehiculo'

class EstadoMovil(models.Model):
    descripcion = models.CharField(max_length=50,unique=True)

    def __unicode__(self):
        return u'%s' % (self.descripcion)
        self.descripcion = self.descripcion.upper()

    def save(self, force_insert=False,force_update=False):
        self.descripcion = self.descripcion.upper()
        super(EstadoMovil, self).save(force_insert,force_update)

    class Meta:
        db_table = 'estado_movil'

class RefTrademark(models.Model):
    id = models.AutoField(primary_key=True)        
    descripcion = models.CharField(max_length=100,unique = True)

    def __unicode__(self):
        return u'%s' % (self.descripcion)
        self.descripcion = self.descripcion.upper()

    def save(self, force_insert=False,force_update=False):
        self.descripcion = self.descripcion.upper()
        super(RefTrademark, self).save(force_insert,force_update)

    class Meta:
        ordering = ['descripcion']
        db_table = 'ref_trademark' 

class RefModelos(models.Model):
    marca           = models.ForeignKey('RefTrademark',related_name="modelos")
    descripcion     = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s' % (self.descripcion)
        self.descripcion = self.descripcion.upper()

    def save(self, force_insert=False,force_update=False):
        self.descripcion = self.descripcion.upper()
        super(RefModelos, self).save(force_insert,force_update)

    class Meta:
        db_table = 'ref_modelos'

class Vehiculo(models.Model):
    dominio=models.CharField(max_length=10,null=True,blank=True)
    anio=models.IntegerField(null=True,blank=True)
    nmotor=models.CharField(max_length=100, null=True,blank=True)
    nchasis=models.CharField(max_length=100,null=True,blank=True)
    modelo=models.ForeignKey('RefModelos',on_delete=models.PROTECT,null=True,blank=True)
    idmarca=models.ForeignKey('RefTrademark',on_delete=models.PROTECT,null=True,blank=True)
    
    def __unicode__(self):
        return u'%s' % (self.dominio)

    class Meta:
        db_table = 'vehiculo'

class Movil(models.Model):
    registro_interno = models.CharField(max_length=6)
    tipo_vehiculo   = models.ForeignKey('TipoVehiculo',related_name='movil',on_delete=models.PROTECT)
    unidad_regional     = models.ForeignKey('UnidadesRegionales',related_name='moviles',on_delete=models.PROTECT)
    dependencia         = models.ForeignKey('Dependencias',related_name='moviles_en',on_delete=models.PROTECT)
    vehiculo            = models.OneToOneField('Vehiculo',on_delete=models.PROTECT,null=True,blank=True)

    def __unicode__(self):
        return u'%s' % (self.registro_interno)
        self.registro_interno = self.registro_interno.upper()

    class Meta:
        db_table = 'movil'

class MovilEstado(models.Model):
    movil   = models.ForeignKey('Movil',related_name='estados',on_delete=models.PROTECT)
    estado  = models.ForeignKey('EstadoMovil',related_name='moviles_estado',on_delete=models.PROTECT)
    fecha   = models.DateTimeField(auto_now=True)
    observaciones = models.TextField(max_length=100,blank=True,null=True)

    class Meta:
        ordering = ['-fecha']
        db_table = 'movil_estados'
