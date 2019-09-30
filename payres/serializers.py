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