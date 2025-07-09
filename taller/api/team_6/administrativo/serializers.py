from rest_framework import serializers
from .models import Edificio, Departamento

class EdificioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Edificio
        fields = ['url', 'id', 'nombre', 'direccion', 'ciudad', 'tipo']

class DepartamentoSerializer(serializers.HyperlinkedModelSerializer):
    edificio = serializers.HyperlinkedRelatedField(view_name='edificio-detail', queryset=Edificio.objects.all())

    class Meta:
        model = Departamento
        fields = ['url', 'id', 'nombre_propietario', 'costo', 'num_cuartos', 'edificio']

