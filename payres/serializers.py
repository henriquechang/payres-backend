from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator
from rest_framework import serializers
from .models import Produto
from .models import Mesa
from .models import PagamentoMesaAuditoria
from .models import ProdutoConsumidoMesaAuditoria


class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produto
        fields = '__all__'


class MesaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mesa
        fields = '__all__'


class PagamentoMesaAuditoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = PagamentoMesaAuditoria
        fields = '__all__'


class ProdutoConsumidoMesaAuditoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProdutoConsumidoMesaAuditoria
        fields = '__all__'


class ProdutoValorMesaSerializer(serializers.Serializer):
    produto__nome = serializers.CharField(max_length=60)
    produto__preco = serializers.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    mesa_id = serializers.IntegerField()
    quantidade = serializers.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(99)])