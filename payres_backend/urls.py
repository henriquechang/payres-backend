"""payres_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from payres.views import ProdutoViewSet
from payres.views import MesaViewSet
from payres.views import ProdutoConsumidoMesaAuditoriaViewSet
from payres.views import PagamentoMesaAuditoriaViewSet
from payres.views import ProdutoValorMesaViewSet
from payres.views import UpdatePagamentoMesaViewSet

router = routers.DefaultRouter()
router.register(
    'produto', ProdutoViewSet, base_name='produto'
)
router.register(
    'mesa', MesaViewSet, base_name='mesa'
)
router.register(
    'pagamento_mesa', PagamentoMesaAuditoriaViewSet, base_name='pagamento_mesa'
)
router.register(
    'produto_consumido_mesa', ProdutoConsumidoMesaAuditoriaViewSet, base_name='produto_consumido_mesa'
)
router.register(
    'produto_valor_mesa', ProdutoValorMesaViewSet, base_name='produto_valor_mesa'
)
router.register(
    'update_pagamento_mesa', UpdatePagamentoMesaViewSet, base_name='update_pagamento_mesa'
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls))
]
