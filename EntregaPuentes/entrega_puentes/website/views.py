from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from .forms import *

# Create your views here.

def inicio(request):
    return render(request, 'website/home.html')

def Domain_form(request):
    if request.method == "POST":
        formulario1 = categoria(request.POST)
        if formulario1.is_valid():
            info = formulario1.cleaned_data
            domain_f = category(domain_name = info["dominio"], owner = info["propietario"], attribute_quantity = info["cantidad_atributos"])
            domain_f.save()
            return render(request, "website/home.html")
    else:
        formulario1 = categoria()
    return render(request, "website/FormularioDominio.html", {"form1":formulario1})

def Task_form(request):
    if request.method == "POST":
        formulario2 = tarea(request.POST)
        if formulario2.is_valid():
            info = formulario2.cleaned_data
            task_f = task(task_name = info["nombre_tarea"], task_deadline = info["fecha_entrega"], task_owner = info["owner_tarea"])
            task_f.save()
            return render(request, "website/home.html")
    else:
        formulario2 = tarea()
    return render(request, "website/FormularioTarea.html", {"form2":formulario2})

def Worker_form(request):
    if request.method == "POST":
        formulario3 = trabajador(request.POST)
        if formulario3.is_valid():
            info = formulario3.cleaned_data
            worker_f = worker(worker_name = info["nombre_trabajador"], worker_domain = info["dominio_trabajador"], worker_email = info["email_trabajador"], worker_phone_number = info["contacto_trabajador"])
            worker_f.save()
            return render(request, "website/home.html")
    else:
        formulario3 = trabajador()
    return render(request, "website/FormularioTrabajador.html", {"form3":formulario3})


def buscarTrabajador(request):
    return render(request, "website/buscador.html")

def search(request):
    if request.GET["worker_name"]:
        buscar = request.GET["worker_name"]
        Trabajador = worker.objects.filter(worker_name__icontains=buscar)
        return render(request, "website/resultado.html", {"Trabajador":Trabajador, "buscar":buscar})
    else:
        mensaje = "Debes ingresar datos."
    return HttpResponse(mensaje)

def trabajadores(request):
    lista_trabajadores = worker.objects.all()
    return render(request, "website/trabajadores.html",{"worker_name":lista_trabajadores})