from django.db import models


# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    cedula=models.CharField(max_length=10,null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class fabricante(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class automovile(models.Model):
    marca_auto = models.CharField(max_length=30)
    color_auto = models.CharField(max_length=10)
    placa_auto = models.CharField(max_length=6)
    fecha_compra=models.DateField(null=True)
    propietario = models.ForeignKey(Persona, on_delete=models.CASCADE, null=True, blank=True, related_name='automoviles')
    fabricante = models.ForeignKey('Fabricante', on_delete=models.CASCADE, null=True, blank=True,related_name='automoviles')
    def __str__(self):
        return f"{self.marca_auto} - {self.color_auto} - {self.placa_auto}"

