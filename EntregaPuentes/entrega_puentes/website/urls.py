from django.urls import path
from website.views import *

urlpatterns = [
    path('', inicio, name = "Inicio"),
    path("DomainForm", Domain_form, name = "FormDomain"),
    path("TaskForm", Task_form, name = "FormTask"),
    path("WorkerForm", Worker_form, name = "FormWorker"),
    path("Buscar", buscarTrabajador, name = "Buscador"),
    path("resultados/", search, name = "Resultado"),
    path("ListaTrabajadores", trabajadores, name = "WorkersList")
]

