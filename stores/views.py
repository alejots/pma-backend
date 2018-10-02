# -*- coding: utf-8 -*-
from rest_framework import mixins, generics, permissions, viewsets
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from stores.models import Product, Unit, Version, Category, Store, ProductInStore
from stores.serializers import VersionSerializer, UnitSerializer, ProductSerializer, CategorySerializer, StoreSerializer# UserSerializer
from stores.permissions import IsOwnerOrReadOnly


'''
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'recetas': reverse('receta-list', request=request, format=format)
    })
'''
class VersionViewSet(viewsets.ModelViewSet):
    queryset = Version.objects.all()
    serializer_class = VersionSerializer

    # Mostrar solo la última versión
    def get_queryset(self):
        result = (self.queryset.filter().order_by('-date')).values()
        response = [{
            'version': result[0]['version'],
            'fecha': result[0]['date']
        }]
        return response

class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


@api_view(['GET'])
def get_all_tokens(request, format=None):
    for user in User.objects.all():
        Token.objects.get_or_create(user=user)
    return Response({'response': 'ok'})
