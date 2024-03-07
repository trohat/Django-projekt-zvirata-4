from django.contrib import admin

from .models import Zvire

# Register your models here.

class ZvireAdmin(admin.ModelAdmin):
    list_display = ("id", "jmeno", "druh", "popis", "vek", "barva")
    list_filter = ("jmeno", "druh", "vek")


admin.site.register(Zvire, ZvireAdmin)





