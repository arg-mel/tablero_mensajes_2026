from django.contrib import admin

from .models import Publicacion


@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    list_display = ["texto", "fecha"]
    search_fields = ["texto"]