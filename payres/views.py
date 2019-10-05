from django.http import HttpResponseNotFound, HttpResponse
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Mesa
from .serializers import MesaSerializer, ProdutoValorMesaSerializer
from .models import Produto
from .serializers import ProdutoSerializer
from .models import ProdutoConsumidoMesaAuditoria
from .serializers import ProdutoConsumidoMesaAuditoriaSerializer
from .models import PagamentoMesaAuditoria
from .serializers import PagamentoMesaAuditoriaSerializer


class ProdutoViewSet(viewsets.ModelViewSet):

    serializer_class = ProdutoSerializer
    queryset = Produto.objects.all()


class MesaViewSet(viewsets.ModelViewSet):

    serializer_class = MesaSerializer
    queryset = Mesa.objects.all()


class ProdutoValorMesaViewSet(viewsets.ModelViewSet):

    serializer_class = ProdutoValorMesaSerializer
    queryset = ProdutoConsumidoMesaAuditoria.objects.all()

    def get_queryset(self):
        queryset = self.queryset.values("produto__preco", "produto__nome", "mesa_id", "quantidade")

        fk = self.request.query_params.get('mesa', None)
        if fk is not None:
            queryset = queryset.filter(mesa=fk, pagamentoAberto=True)

        return queryset


class ProdutoConsumidoMesaAuditoriaViewSet(viewsets.ModelViewSet):

    serializer_class = ProdutoConsumidoMesaAuditoriaSerializer
    queryset = ProdutoConsumidoMesaAuditoria.objects.all()

    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            data = kwargs["data"]

            # check if many is required
            if isinstance(data, list):
                kwargs["many"] = True
        return super(ProdutoConsumidoMesaAuditoriaViewSet, self).get_serializer(*args, **kwargs)


class PagamentoMesaAuditoriaViewSet(viewsets.ModelViewSet):

    serializer_class = PagamentoMesaAuditoriaSerializer
    queryset = PagamentoMesaAuditoria.objects.all()

    def create(self, request):
        queryset = self.queryset
        fk = self.request.query_params.get('mesa', None)
        if fk is not None:
            mesa = Mesa.objects.get(id=fk)
            pagnovo = PagamentoMesaAuditoria(
                valorPago=self.request.data["valorPago"],
                mesa=mesa,
                pagamentoAberto=True
            )
            pagnovo.save()
        serializer = PagamentoMesaAuditoriaSerializer(queryset, many=True)
        return Response(serializer.data)

    def list(self, request):
        queryset = self.queryset

        fk = self.request.query_params.get('mesa', None)
        if fk is not None:
            queryset = queryset.filter(mesa=fk, pagamentoAberto=True)

        serializer = PagamentoMesaAuditoriaSerializer(queryset, many=True)
        return Response(serializer.data)


class UpdatePagamentoAbertoViewSet(viewsets.ViewSet):

    queryset_pagamento = PagamentoMesaAuditoria.objects.all()
    queryset_produtos = ProdutoConsumidoMesaAuditoria.objects.all()

    def create(self, request):
        queryset_pagamento = self.queryset_pagamento
        queryset_produtos = self.queryset_produtos
        fk = self.request.query_params.get('mesa', None)
        if fk is not None:
            mesa = Mesa.objects.get(id=fk)
            queryset_produtos.filter(mesa=mesa, pagamentoAberto=True).update(pagamentoAberto=False)
            queryset_pagamento.filter(mesa=mesa, pagamentoAberto=True).update(pagamentoAberto=False)
        return Response(data={"message": "Update realizado com sucesso"}, status=status.HTTP_201_CREATED)
