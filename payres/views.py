from decimal import Decimal

from django.http import HttpResponseBadRequest, HttpResponse
from rest_framework import viewsets, status
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
            produtos_consumidos = ProdutoConsumidoMesaAuditoria.objects.all().filter(pagamentoAberto=True, mesa=mesa)
            valor_total_consumido = 0
            valor_total_pago = 0
            valor_pago = round(Decimal(self.request.data["valorPago"]), 2)
            for consumo in produtos_consumidos:
                valor_total_consumido += consumo.quantidade*consumo.produto.preco
            produtos_pagos = PagamentoMesaAuditoria.objects.all().filter(pagamentoAberto=True, mesa=mesa)
            for pagamento in produtos_pagos:
                valor_total_pago += pagamento.valorPago
            if valor_total_consumido == 0:
                return Response(data={"message": "Não existem produtos consumidos para essa mesa"}, status=status.HTTP_400_BAD_REQUEST)
            if valor_pago <= 0:
                return Response(data={"message": "Favor inserir um valor maior que 0."}, status=status.HTTP_400_BAD_REQUEST)
            valor_restante = valor_total_consumido - valor_total_pago
            if valor_pago > valor_restante:
                return Response(data={"message": "O valor inserido é maior que o valor restante a ser pago"}, status=status.HTTP_400_BAD_REQUEST)
            pagnovo = PagamentoMesaAuditoria(
                valorPago=valor_pago,
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


class UpdatePagamentoMesaViewSet(viewsets.ViewSet):

    queryset_pagamento = PagamentoMesaAuditoria.objects.all()
    queryset_produtos = ProdutoConsumidoMesaAuditoria.objects.all()

    def create(self, request):
        queryset_pagamento = self.queryset_pagamento
        queryset_produtos = self.queryset_produtos
        fk = self.request.query_params.get('mesa', None)
        if fk is not None:
            mesa = Mesa.objects.get(id=fk)
            produtos_consumidos = ProdutoConsumidoMesaAuditoria.objects.all().filter(pagamentoAberto=True, mesa=mesa)
            valor_total_consumido = 0
            valor_total_pago = 0
            for consumo in produtos_consumidos:
                valor_total_consumido += consumo.quantidade * consumo.produto.preco
            if valor_total_consumido == 0:
                return Response(data={"message": "Não existem produtos consumidos para essa mesa"}, status=status.HTTP_400_BAD_REQUEST)
            produtos_pagos = PagamentoMesaAuditoria.objects.all().filter(pagamentoAberto=True, mesa=mesa)
            for pagamento in produtos_pagos:
                valor_total_pago += pagamento.valorPago
            valor_restante = valor_total_consumido - valor_total_pago
            if valor_restante > 0:
                return Response(data={"message": "Ainda há pagamentos pendentes"}, status=status.HTTP_400_BAD_REQUEST)
            queryset_produtos.filter(mesa=mesa, pagamentoAberto=True).update(pagamentoAberto=False)
            queryset_pagamento.filter(mesa=mesa, pagamentoAberto=True).update(pagamentoAberto=False)
            return Response(data={"message": "Conta fechada"}, status=status.HTTP_201_CREATED)
        return Response(data={"message": "O id da mesa é necessário para a atualização"}, status=status.HTTP_400_BAD_REQUEST)
