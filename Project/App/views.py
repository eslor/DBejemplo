from django.shortcuts import render

from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .models import Cat
from .serializers import CatSerializer

class ListCatAPIView(ListAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

class CreateCatAPIView(CreateAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

class UpdateCatAPIView(UpdateAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

class DeleteCatAPIView(DestroyAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer