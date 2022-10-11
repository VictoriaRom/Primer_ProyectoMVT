from concurrent.futures.process import _MAX_WINDOWS_WORKERS
from django.db import models

class Persona(models.Model):
    nombre= models.CharField(max_length=30)  #Nombre del familiar
    apellido=models.CharField(max_length=30) #Apellido del familiar
    edad=models.IntegerField()                #Edad del familiar
    fecha_registro=models.DateField()        #fecha 
    email=models.CharField(max_length=30)         #correo electronico del familiar
