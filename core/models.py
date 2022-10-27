from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models


# Create your models here.

class vacinas(models.Model):
    vac_tipo_vacina = models.CharField(max_length = 120)
    vac_lote = models.CharField(max_length = 45)
    vac_fabricante = models.CharField(max_length = 45)
    vac_descricao = models.CharField(max_length = 300)
    vac_quantidade = models.IntegerField()
    vac_disponibilidade = models.BooleanField()
    vac_contraindicacao = models.CharField(max_length = 300)
    vac_reacoes = models.CharField(max_length = 300)
    vac_data_fabricacao = models.DateField()
    vac_data_validade = models.DateField()
    vac_data_recebimento = models.DateField()
    def __str__(self):
        return (self.vac_tipo_vacina)
    class Meta:
        verbose_name_plural = "Vacinas"

class postos(models.Model):
    pos_nome = models.CharField(max_length = 120)
    pos_cep = models.CharField(max_length = 45)
    pos_rua = models.CharField(max_length = 45)
    pos_bairro = models.CharField(max_length = 45)
    pos_numero = models.IntegerField()
    pos_logradouro = models.CharField(max_length = 45)
    pos_telefone = models.CharField(max_length = 45)
    def __str__(self):
        return (self.pos_nome)
    class Meta:
        verbose_name_plural = "Postos"
# Create your models here.