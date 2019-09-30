from django.db import models


class Produto(models.Model):

    nome = models.CharField(max_length=60)
    preco = models.DecimalField(max_digits=8, decimal_places=2)


class Mesa(models.Model):

    valorTotal = models.DecimalField(max_digits=8, decimal_places=2)


class PagamentoMesaAuditoria(models.Model):
    valorPago = models.DecimalField(max_digits=8, decimal_places=2)
    pagamentoAberto = models.BooleanField()
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)


class ProdutoConsumidoMesaAuditoria(models.Model):
    pagamentoAberto = models.BooleanField()
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)


