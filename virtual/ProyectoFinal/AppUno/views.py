from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from AppUno.forms import *
from django.urls import reverse_lazy

def abuelos(request):
    return render(request, "AppUno/abuelos.html")

def padres(request):
    return render(request, "AppUno/padres.html")

def primos(request):
    return render(request, "AppUno/primos.html")

def inicio(request):
    return render(request, "AppUno/inicio.html")
"""def abueloFormulario(request):
    if request.method=="post":
        nombre = request.post["Nombre"]
        edad = request.post["Edad"]
        abuelo = Abuelos(Nombre=nombre, Edad=edad)
        abuelo.save()
        return render (request, "AppUno/inicio.html", {"mensaje": "Abuelo guardado correctamente"})
        pass
    else:
        return render (request, "AppUno/abueloFormulario.hmtl")"""

def abueloFormulario(request):
    if request.method=="post":
        form = AbueloForm(request.post)
        if form.is_valid():
            informacion= form.cleaned_data
            nombre = informacion["nombre"]
            edad = informacion["edad"] 
            abuelo= Abuelos(Nombre=nombre, Edad=edad)
            abuelo.save()
            return render(request, "AppUno/inicio.html", {"mensaje": "Abuelo guardado correctamente"})
        else: 
            return render(request, "AppUno/abueloFormulario.html", {"form":form, "mensaje":"Informacion no valida"})
        pass

    else:
        formulario= AbueloForm()
        return render (request, "AppUno/abueloFormulario.html", {"form": formulario}) 

def primoFormulario(request):
    if request.method=="post":
        form = PrimoForm(request.post)
        if form.is_valid():
            informacion= form.cleaned_data
            nombre = informacion["nombre"]
            edad = informacion["edad"] 
            primo= Primos(Nombre=nombre, Edad=edad)
            primo.save()
            return render(request, "AppUno/inicio.html", {"mensaje": "Primo guardado correctamente"})
        else: 
            return render(request, "AppUno/primoFormulario.html", {"form":form, "mensaje":"Informacion no valida"})
        pass

    else:
        formulario= PrimoForm()
        return render (request, "AppUno/primoFormulario.html", {"form": formulario})

def padreFormulario(request):
    if request.method=="post":
        form = PadreForm(request.post)
        if form.is_valid():
            informacion= form.cleaned_data
            nombre = informacion["nombre"]
            edad = informacion["edad"] 
            abuelo= Padres(Nombre=nombre, Edad=edad)
            abuelo.save()
            return render(request, "AppUno/inicio.html", {"mensaje": "Padre guardado correctamente"})
        else: 
            return render(request, "AppUno/padreFormulario.html", {"form":form, "mensaje":"Informacion no valida"})
        pass

    else:
        formulario= PadreForm()
        return render (request, "AppUno/padreFormulario.html", {"form": formulario})

def busquedaNombre(request):
    return render(request, "AppUno/busquedaNombre.html")

def buscar(request):
    nombre= request.get["nombre"]
    if nombre!="":
        primos= Primos.objects.filter(nombre__icontains=nombre)
        return render(request, "AppUno/resultadosBusqueda.html", {"primos": primos})
    else:
        return render(request, "AppUno/busquedaNombre.html", {"mensaje":"Ingrese un nombre para buscar"})
# Create your views here.
