from django.db import models

# Create your models here.
class Gatos_en_adopcion(models.Model):
    
    nombre = models.CharField(max_length=20)
    raza = models.CharField(max_length=20)
    fecha_encontrado = models.DateField()
    edad = models.FloatField()
    foto = models.ImageField(upload_to='fotos_gatos')

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    rut = models.CharField(max_length=15)
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    domicilio = models.TextField()
    fecha_registro = models.DateTimeField(auto_now=True)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre
