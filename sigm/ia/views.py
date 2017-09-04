# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
import models
import forms
import json
# Create your views here.

@login_required(login_url='/login/')
def index(request):
    periodo = models.Periodo.objects.last()
    return render(request, 'index.html', {'periodo': periodo})
# end def

def logoutUsers(request):
    logout(request)
    return redirect('/')
# end def

def abrirPeriodo(request):
    old = models.Periodo.objects.last()
    if old:
        num = old.numero+1
        nuevo = models.Periodo(numero=num, cerrado=False)
        nuevo.save()
    else:
        nuevo = models.Periodo(numero=1, cerrado=False)
        nuevo.save()
    # end if
    return redirect('/')
# end def

def cerrarPeriodo(request, pk):
    periodo = models.Periodo.objects.filter(id=pk).first()
    if periodo:
        periodo.cerrado = True
        periodo.save()
    return redirect('/')
# end def


def registrar_e(request):
    if request.method == "POST":
        form = forms.EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/matricula/estudiante/')
        else:
            return render(request, 'registro_e.html', {'form': form})
        # end if
    return render(request, 'registro_e.html', {'form': forms.EstudianteForm()})
# end if


def matricula_e(request):
    identificacion = request.GET.get('identificacion', False)
    mensaje = ""
    if identificacion:
        estudiante = models.Estudiante.objects.filter(identificacion=identificacion).first()
        if estudiante:
            periodo = models.Periodo.objects.last()
            if periodo:
                matricula = models.Matricula.objects.filter(estudiante=estudiante, periodo=periodo)
                if matricula:
                    mensaje = "Ya esta matriculado"
                else:
                    if not periodo.cerrado:
                        matricula = models.Matricula(periodo=periodo, estudiante=estudiante)
                        matricula.save()
                        mensaje = "Matriculado"
                    else:
                        mensaje = "Periodo cerrado, no se puede matricular"
            else:
                mensaje = "No se puede matricular"
        else:
            mensaje = "No hay ningun estudiante con este codigo"
    return render(request, 'matricula.html', {"mensaje": mensaje})
# end def


def desertados(request):
    return render(request, 'desertados.html', {})
# end def


def listaMatriculados(request):
    periodo = models.Periodo.objects.last()
    estudiante = models.Estudiante.objects.all().exclude(matricula__periodo=periodo).values('latitud', 'longitud')
    data = list(estudiante)
    return HttpResponse(json.dumps(data), content_type="text/json")
# end def
