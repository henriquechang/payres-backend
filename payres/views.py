from rest_framework import viewsets
from .models import Mesa
from .serializers import MesaSerializer
from .models import Produto
from .serializers import ProdutoSerializer
from .models import ProdutoConsumidoMesaAuditoria
from .serializers import ProdutoConsumidoMesaAuditoriaSerializer
from rest_framework.decorators import action


class ProdutoViewSet(viewsets.ModelViewSet):

    serializer_class = ProdutoSerializer
    queryset = Produto.objects.all()


class MesaViewSet(viewsets.ModelViewSet):

    serializer_class = MesaSerializer
    queryset = Mesa.objects.all()
