from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import Person, Category
from .serializers import PoetSerializers

class CRUDPoet(mixins.CreateModelMixin,
               mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin,
               mixins.ListModelMixin,
               GenericViewSet):
    queryset = Person.objects.all()[:2]
    serializer_class = PoetSerializers

    @action(detail=True, methods=['get'])
    def zakh1dvna(self, request, pk=None):
        data = Category.objects.get(pk=pk)
        return Response({'cats': data.name})

# class ListCreatePoet(generics.ListCreateAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PoetSerializers
# class UpdateDeleteRetrivePoet(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PoetSerializers
