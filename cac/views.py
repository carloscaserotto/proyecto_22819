from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse


# Create your views here.
def index(request):
    if(request.method =='GET'):
        titulo = 'Titulo cuando se accede por GET'
    else:
        titulo = f'Titulo cuando se accede por otro metodo {request.method}'
    parameters_get = request.GET.get('otro')
    return HttpResponse(f"""
            <h1>{titulo}</h1>
            <p>{parameters_get}</p>
            """)

    pass

def quienes_somos(request):
    #return redirect('saludar_por_defecto')
    return redirect(reverse('saludar', kwargs={'nombre':'Carli'}))

def hola_mundo(request):
    return HttpResponse("Hola mundo Django")

def saludar(request, nombre=""):
    return HttpResponse(f"""
            <h1>Hola mundo Django - {nombre}</h1>
            <p> estoy haciendo una prueba </p>
            """)

def ver_proyectos(request, anio, mes):
    return HttpResponse(f"""
            <h1>Proyecto - {request}</h1>
            <h1>Proyecto - {anio}</h1>
            <h2>Proyecto - {mes}</h2>
            <p> estoy haciendo una prueba </p>
            """)
def ver_proyectos_anio(request, anio):
    return HttpResponse(f"""
            <h1>Proyecto - {anio}</h1>
            """)
def ver_proyecto(request, nombre, numero):
    return HttpResponse(f"""
            <h1>Nombre proyecto: {nombre}</h1>
            <h2>Numero de proyecto: {numero}</h2>
            <p> estoy haciendo una prueba </p>
            """)
def cursos_detalle(request, nombre_curso):
    return HttpResponse(f"""
            <h1> {nombre_curso} </h1>
    """)
def cursos(request,nombre):
    return HttpResponse(f"""
            <h1> {nombre} </h1>
    """)
