from django.db import models
from django.contrib.auth.models import User

class CategoriaEvento(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Local(models.Model):
    nome = models.CharField(max_length=150)
    endereco = models.CharField(max_length=300)
    capacidade = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nome

class Palestrante(models.Model):
    nome = models.CharField(max_length=150)
    mini_bio = models.TextField()
    foto = models.ImageField(upload_to='palestrantes/', blank=True, null=True)

    def __str__(self):
        return self.nome

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data_hora = models.DateTimeField()
    local = models.ForeignKey(Local, on_delete=models.SET_NULL, null=True)
    banner_evento = models.ImageField(upload_to='eventos_banners/', blank=True, null=True)
    categoria = models.ForeignKey(CategoriaEvento, on_delete=models.SET_NULL, null=True)
    palestrantes = models.ManyToManyField(Palestrante)

    def __str__(self):
        return self.titulo


class Inscricao(models.Model):
    participante = models.ForeignKey(User, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    data_inscricao = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('participante', 'evento')

    def __str__(self):
        return f'{self.participante.username} em {self.evento.titulo}'