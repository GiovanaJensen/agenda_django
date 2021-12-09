from django.contrib import admin
from core.models import Evento

# Register your models here.
class EventoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "dt_evento", "dt_criacao")
    list_filter = ("usuario", "titulo",)

admin.site.register(Evento, EventoAdmin)