# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime


class Comentario(models.Model):
    local = models.CharField(max_length=100)
    avaliacao = models.TextField(blank=False, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'turismo_avaliacao'

    def __str__(self):
    	return self.avaliacao

class Eventos(models.Model):
    data_evento = models.DateTimeField()
    descricao = models.CharField(max_length=100)
    local = models.CharField(max_length=100)

    class Meta:
        db_table = 'eventos'
    def get_dia(self):
        return self.data_evento.strftime('%d')
    def get_mes(self):
        return self.data_evento.strftime('%b')