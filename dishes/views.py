from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Dish, Cuisine, DishImage
from .permissions import IsManagersOrReadOnly
from .serializers import *


class CuisineModelViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsManagersOrReadOnly]

    def get_queryset(self):
        return Cuisine.objects.all()


    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return ReadCuisineSerializer
        return WriteCuisineSerializer

    @action(detail=True, methods=['get'])
    def Dishes(self, request, pk=None):
        dish_category = Dish.objects.filter(cuisine=pk)
        serializer = ReadDishSerializer(dish_category, many=True)
        return Response(serializer.data)


class DishModelViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsManagersOrReadOnly]

    def get_queryset(self):
        return Dish.objects.select_related("restaurant")

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return ReadDishSerializer
        return WriteDishSerializer


    @action(detail=True, methods=['get'])
    def dishImages(self, request, pk=None):
        dish_image = DishImage.objects.filter(dish=pk)
        serializer = ReadDishImageSerializer(dish_image, many=True)
        return Response(serializer.data)




class DishImageModelViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsManagersOrReadOnly]

    def get_queryset(self):
        return DishImage.objects.select_related("dish")

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return ReadDishImageSerializer
        return WriteDishImageSerializer
