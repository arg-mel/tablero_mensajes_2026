from django.test import TestCase
from django.urls import reverse

from .models import Publicacion


class PruebasPublicacion(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.publicacion = Publicacion.objects.create(texto="¡Esto es una prueba!")

    def test_contenido_modelo(self):
        self.assertEqual(self.publicacion.texto, "¡Esto es una prueba!")

    def test_url_existe_ubicacion_correcta(self):
        respuesta = self.client.get("/")
        self.assertEqual(respuesta.status_code, 200)

    def test_pagina_inicio(self):
        respuesta = self.client.get(reverse("inicio"))
        self.assertEqual(respuesta.status_code, 200)
        self.assertTemplateUsed(respuesta, "lista_publicaciones.html")
        self.assertContains(respuesta, "¡Esto es una prueba!")