# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from rest_framework import serializers
from django.contrib.auth.models import User

from stores.models import Product, Unit, Version, Category, Store, ProductInStore

class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Version
        fields = '__all__'

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    unit = UnitSerializer(read_only=True)
    class Meta:
        model = Product
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'

'''
class RecetaSerializer(serializers.ModelSerializer):

    ingredientes = IngredienteSerializer(many=True, read_only=True)
    implementos = ImplementoSerializer(many=True, read_only=True)
    pasos = PasoSerializer(many=True, read_only=True)
    me_gustas = serializers.IntegerField(
        source='me_gustas.count',
        read_only=True
    )
    compartidos = serializers.IntegerField(
        source='compartidos.count',
        read_only=True
    )

    class Meta:
        model = Receta
        fields = ('id', 'nombre', 'imagen', 'region', 'porciones', 'tiempo_preparacion', 'me_gustas', 'compartidos',
                  'ingredientes', 'pasos', 'implementos', 'sugerencia',  'is_active')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    proyectos = serializers.HyperlinkedRelatedField(
        many=True, view_name='receta-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'recetas') '''
