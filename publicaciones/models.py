from django.db import models


class Publicacion(models.Model):
    texto = models.TextField()
