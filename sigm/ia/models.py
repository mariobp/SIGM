# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    identificacion = models.CharField(max_length=100)
    latitud = models.FloatField(null=True, blank=True)
    longitud = models.FloatField(null=True, blank=True)

    def __unicode__(self):
        return u"%s %s" % (self.nombre, self.apellidos)
    # end def
# end class

class Administrador(User):
    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)
    # end def
# end class

class Periodo(models.Model):
    numero = models.IntegerField(unique=True)
    cerrado = models.BooleanField(default=False)
# end class

class Matricula(models.Model):
    periodo = models.ForeignKey(Periodo)
    estudiante = models.ForeignKey(Estudiante)
# end class
