from django.db import models

# Create your models here.


class Funcionario(models.Model):
    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )
    sobrenome = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )

    cpf = models.CharField(
        max_length=14,
        null=False,
        blank=False,
    )

    tempo_de_servico = models.PositiveIntegerField(
        default=0,
        null=False,
        blank=False,
    )

    remuneracao = models.DecimalField(
        max_digits=8,
        decimal_places=3,
        null=False,
        blank=False,
        verbose_name='Remuneração'
    )

    def __str__(self):
        return self.nome
