from django.db import models

# Create your models here.
class Producto(models.Model):

    nombre=models.CharField(max_length=40)

    marca=models.CharField(max_length=40)

    codigo=models.IntegerField()


class Cliente(models.Model):

    nombre=models.CharField(max_length=40)

    apellido=models.CharField(max_length=40)

    dni=models.IntegerField()


class Empleado(models.Model):

    nombre=models.CharField(max_length=40)

    apellido=models.CharField(max_length=40)

    dni=models.IntegerField()