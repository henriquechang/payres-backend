from decimal import Decimal

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Produto(models.Model):

    nome = models.CharField(max_length=60)
    preco = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])


class Mesa(models.Model):

    valorTotal = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])


class PagamentoMesaAuditoria(models.Model):

    valorPago = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    pagamentoAberto = models.BooleanField()
    mesa = models.ForeignKey(Mesa, on_delete=models.PROTECT)


class ProdutoConsumidoMesaAuditoria(models.Model):

    pagamentoAberto = models.BooleanField()
    quantidade = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(99)])
    mesa = models.ForeignKey(Mesa, on_delete=models.PROTECT, related_name='mesa')
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name='produto')




