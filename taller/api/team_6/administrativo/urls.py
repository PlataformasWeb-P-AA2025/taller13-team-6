from django.urls import path, include
from rest_framework.routers import DefaultRouter
from administrativo.views import EdificioViewSet, DepartamentoViewSet

router = DefaultRouter()
router.register(r'edificios', EdificioViewSet,basename='edificio')
router.register(r'departamentos', DepartamentoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
