from django.contrib import admin

from .models import Zvire, Pavilon

# Register your models here.

class ZvireAdmin(admin.ModelAdmin):
    list_display = ("id", "jmeno", "druh", "popis", "vek", "barva", "pavilon")
    list_filter = ("jmeno", "druh", "vek")

class PavilonAdmin(admin.ModelAdmin):
    list_display = ("id", "jmeno", "umisteni")

admin.site.register(Zvire, ZvireAdmin)

admin.site.register(Pavilon, PavilonAdmin)





