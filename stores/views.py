# -*- coding: utf-8 -*-
from rest_framework import mixins, generics, permissions, viewsets
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from stores.models import Version
from stores.serializers import VersionSerializer # UserSerializer
from stores.permissions import IsOwnerOrReadOnly


'''
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'recetas': reverse('receta-list', request=request, format=format)
    })


class RecetaViewSet(viewsets.ModelViewSet):

    queryset = Receta.objects.all()
    serializer_class = RecetaSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class IngredienteViewSet(viewsets.ModelViewSet):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ImplementoViewSet(viewsets.ModelViewSet):
    queryset = Implemento.objects.all()
    serializer_class = ImplementoSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

'''
class VersionViewSet(viewsets.ModelViewSet):
    queryset = Version.objects.all()
    serializer_class = VersionSerializer

    # Mostrar solo la última versión
    def get_queryset(self):
        result = (self.queryset.filter().order_by('-date')).values()

        response = [
            {
                'version': result[0]['version'],
                'fecha': result[0]['date']
            },

        ]
        return response


@api_view(['GET'])
def get_all_tokens(request, format=None):
    for user in User.objects.all():
        Token.objects.get_or_create(user=user)
    return Response({'response': 'ok'})
