from django.test import TestCase
from apps.Gatos.models import Gatos_en_adopcion
from apps.Gatos.forms import  Gatos_en_adopcion_form

class GatosFormCase(TestCase):
        
    def test_valid_form(self):
        gatos = Gatos_en_adopcion.objects.create(nombre='altair',fecha_encontrado=10/10/1010, edad=2,raza='pelucon')
        data = {'nombre': gatos.nombre, 'fecha_encontrado': gatos.fecha_encontrado,'edad': gatos.edad,'raza':gatos.raza }
        form = Gatos_en_adopcion_form(data=data)
        self.assertTrue(form.is_valid())
        
    def test_invalid_form(self):
        gatos = Gatos_en_adopcion.objects.create(nombre='ezio',fecha_encontrado=10/10/1000, edad=20,raza='pelucon')
        data = {'nombre': gatos.nombre, 'fecha_encontrado': gatos.fecha_encontrado,'edad': gatos.edad,'raza':gatos.raza }
        form = Gatos_en_adopcion_form(data=data)
        self.assertFalse(form.is_valid())
