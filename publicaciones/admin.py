from django.contrib import admin

from .models import Publicacion


@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    list_display = ["texto", "autor", "fecha"]
    search_fields = ["texto"]
    list_filter = ["fecha"]