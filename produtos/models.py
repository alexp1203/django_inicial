from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()

    def __srt__(self) -> str:
        return self.nome