from django.test import TestCase
from apps.Gatos.models import Gatos_en_adopcion
from apps.Gatos.forms import Gatos_en_adopcion_form

class CarreraTestCase(TestCase):
    def setUp(self):
        Gatos_en_adopcion.objects.create(nombre="AAA",semestres=4, mensualidad=10000)
        Gatos_en_adopcion.objects.create(nombre="BBB",semestres=6, mensualidad=20000)

    def test_ingresar_carreras(self):
        """Las carreras se registran correctamente en la BD"""
        gato_1 = Gatos_en_adopcion.objects.get(nombre="AAA")
        gato_2 = Gatos_en_adopcion.objects.get(nombre="BBB")
        self.assertEqual(gato_1.semestres, 4)
        self.assertEqual(gato_2.semestres, 6)
