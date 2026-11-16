from django.template.defaultfilters import date
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Publicacion


class PruebasPublicacion(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.publicacion = Publicacion.objects.create(texto="¡Esto es una prueba!")

    def test_contenido_modelo(self):
        self.assertEqual(self.publicacion.texto, "¡Esto es una prueba!")

    def test_str_modelo(self):
        self.assertEqual(str(self.publicacion), "¡Esto es una prueba!")

    def test_fecha_en_pagina(self):
        fecha_local = timezone.localtime(self.publicacion.fecha)
        texto_fecha = date(fecha_local, r"j \d\e F, H:i")
        respuesta = self.client.get(reverse("inicio"))
        self.assertContains(respuesta, texto_fecha)

    def test_url_existe_ubicacion_correcta(self):
        respuesta = self.client.get("/")
        self.assertEqual(respuesta.status_code, 200)

    def test_pagina_inicio(self):
        respuesta = self.client.get(reverse("inicio"))
        self.assertEqual(respuesta.status_code, 200)
        self.assertTemplateUsed(respuesta, "lista_publicaciones.html")
        self.assertContains(respuesta, "¡Esto es una prueba!")
        self.assertContains(respuesta, "Anónimo")



class PruebasSinPublicaciones(TestCase):
    def test_pagina_vacia(self):
        respuesta = self.client.get(reverse("inicio"))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "Todavía no hay publicaciones.")
        self.assertContains(respuesta, "Hay 0 publicaciones.")