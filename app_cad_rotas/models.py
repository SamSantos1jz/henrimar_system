from django.db import models

class Rotas(models.Model):
    id_rotas = models.AutoField(primary_key=True)
    rota = models.TextField(max_length=255)
    motorista = models.TextField(max_length=255)