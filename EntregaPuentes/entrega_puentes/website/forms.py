from tkinter.ttk import Style
from django import forms

class categoria(forms.Form):

    dominio = forms.CharField(max_length=40, widget=forms.TextInput(attrs={"placeholder":"Dominio"}), help_text='Nombre del dominio', label="")
    propietario = forms.CharField(max_length=40, widget=forms.TextInput(attrs={"placeholder":"Owner"}), help_text='Propietario del dominio', label="")
    cantidad_atributos = forms.IntegerField(widget=forms.TextInput(attrs={"placeholder":"Número de Atributos"}), help_text='Cantidad de atributos del dominio', label="")

class tarea(forms.Form):

    nombre_tarea = forms.CharField(max_length= 20, widget=forms.TextInput(attrs={"placeholder":"Tarea"}), help_text='Nombre de la tarea', label="")
    fecha_entrega = forms.DateField(widget=forms.TextInput(attrs={"placeholder":"Fecha de entrega"}), help_text='Fecha limite de entrega de la tarea', label="")
    owner_tarea = forms.CharField(max_length= 40, widget=forms.TextInput(attrs={"placeholder":"Owner de la tarea"}), help_text='Persona a la que corresponde realizar la tarea', label="" )

class trabajador(forms.Form):

    nombre_trabajador = forms.CharField(max_length= 40, widget=forms.TextInput(attrs={"placeholder":"Trabajador"}), help_text='Nombre del trabajador', label="")
    dominio_trabajador = forms.CharField(max_length=40, widget=forms.TextInput(attrs={"placeholder":"Dominio asignado"}), help_text='Dominio del trabajador', label="")
    email_trabajador = forms.EmailField(widget=forms.TextInput(attrs={"placeholder":"Email"}), help_text='Dirección de correo del trabajador', label="")
    contacto_trabajador = forms.IntegerField(widget=forms.TextInput(attrs={"placeholder":"Celular"}), help_text='Número de contacto del trabajador', label="")