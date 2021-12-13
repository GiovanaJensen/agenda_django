from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    dt_evento = models.DateTimeField()
    dt_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'evento'
    def __str__(self):
        return self.titulo
    def get_data_evento(self):
        return self.dt_evento.strftime('%d/%m/%Y %H:%M')