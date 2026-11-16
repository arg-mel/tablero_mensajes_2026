from django.db import models


class Publicacion(models.Model):
    texto = models.TextField()
    fecha = models.DateTimeField("fecha de publicación", auto_now_add=True)

    class Meta:
        ordering = ["-fecha"]
        verbose_name = "publicación"
        verbose_name_plural = "publicaciones"

    def __str__(self):
        return self.texto[:50]