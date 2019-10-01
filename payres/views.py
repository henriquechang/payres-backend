from rest_framework import viewsets
from .models import Mesa
from .serializers import MesaSerializer
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


class ProdutoConsumidoMesaAuditoriaViewSet(viewsets.ModelViewSet):

    serializer_class = ProdutoConsumidoMesaAuditoriaSerializer
    queryset = ProdutoConsumidoMesaAuditoria.objects.all()


class  PagamentoMesaAuditoriaViewSet(viewsets.ModelViewSet):

    serializer_class = PagamentoMesaAuditoriaSerializer
    queryset = PagamentoMesaAuditoria.objects.all()
