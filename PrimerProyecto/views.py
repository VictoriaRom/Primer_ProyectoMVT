from pickle import PERSID
from re import template
from xmlrpc.client import NOT_WELLFORMED_ERROR
from AppCoder.models import Persona
from django.http import HttpResponse
from datetime import datetime
from django.template import Context,Template,loader
import random

def crear_personas(request,nombre,apellido,edad,fecha_registro,email):


    persona = Persona(nombre=nombre, apellido=apellido, edad=edad, fecha_registro=fecha_registro, email=email)
    persona.save()
    template=loader.get_template("crear_persona.html")
    template_renderizado=template.render({"persona":persona})

    return HttpResponse (" ")


def ver_personas(request):

    persona = Persona.objects.all()
    template=loader.get_template("ver_personas.html")
    template_renderizado=template.render({"personas":Persona})

    return HttpResponse ("template_renderizado")






    
    
    
    

