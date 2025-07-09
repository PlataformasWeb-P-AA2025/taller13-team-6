from django.urls import path, include
# se importa las vistas de la aplicación
from Departamentos import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'edificios', views.EdificioViewSet)
router.register(r'departamentos', views.DepartamentoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', views.index, name='index'),
        path('departamento/<int:id>', views.obtener_departamento,
            name='obtener_departamento'),
    path('edificio/<int:id>', views.obtener_edificio,
            name='obtener_edificio'),
    path('departamento/crear', views.crear_departamento,
            name='crear_departamento'),
    path('edificio/crear', views.crear_edificio,
            name='crear_edificio'),
    pahth('departamento/editar/<int:id>', views.editar_departamento,
            name='editar_departamento'),