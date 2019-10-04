from rest_framework import viewsets
from .models import Mesa
from .serializers import MesaSerializer, ProdutoValorMesaSerializer
from .models import Produto
from .serializers import ProdutoSerializer
from .models import ProdutoConsumidoMesaAuditoria
from .serializers import ProdutoConsumidoMesaAuditoriaSerializer
from .models import PagamentoMesaAuditoria
from .serializers import PagamentoMesaAuditoriaSerializer
from django.core import serializers


class ProdutoViewSet(viewsets.ModelViewSet):

    serializer_class = ProdutoSerializer
    queryset = Produto.objects.all()


class MesaViewSet(viewsets.ModelViewSet):

    serializer_class = MesaSerializer
    queryset = Mesa.objects.all()


class ProdutoConsumidoMesaAuditoriaViewSet(viewsets.ModelViewSet):

    serializer_class = ProdutoValorMesaSerializer;
    queryset = ProdutoConsumidoMesaAuditoria.objects.all()

    def get_queryset(self):
        queryset = self.queryset

        fk = self.request.query_params.get('mesa', None)
        if fk is not None:
            queryset = queryset.filter(mesa=fk, pagamentoAberto=True).values("produto__preco", "produto__nome", "mesa_id", "quantidade")

        return queryset


class  PagamentoMesaAuditoriaViewSet(viewsets.ModelViewSet):

    serializer_class = PagamentoMesaAuditoriaSerializer
    queryset = PagamentoMesaAuditoria.objects.all()
