from django.contrib.auth.models import User
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from dishes.models import Dish, Cuisine
from dishes.permissions import IsManagersOrReadOnly
from dishes.serializers import ReadDishSerializer, ReadCuisineSerializer
from .models import Restaurant, Sector
from .serializers import *


# Create your views here.
class RestaurantModelViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsManagersOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['rating', "name"]

    def get_queryset(self):
        return Restaurant.objects.select_related("district", "sector", "owner")

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return ReadRestaurantSerializer
        return WriteRestaurantSerializer

    @action(detail=True, methods=['get'])
    def Cuisines(self, request, pk=None):
        resto_cuis = Cuisine.objects.filter(restaurant=pk)
        serializer = ReadCuisineSerializer(resto_cuis, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def Dishes(self, request, pk=None):
        resto_dish = Dish.objects.filter(restaurant=pk)
        serializer = ReadDishSerializer(resto_dish, many=True)
        return Response(serializer.data)




class favouriteRestaurant(viewsets.ModelViewSet):
    queryset = Restaurant.objects.filter(rating = 5)[:8]
    serializer_class = ReadRestaurantSerializer



class OwnerModelViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type']

    def get_queryset(self):
        return Owner.objects.all()

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return ReadOwnerSerializer
        return WriteOwnerSerializer

    @action(detail=True, methods=['get'])
    def Restaurants(self, request, pk=None):
        owner_resto = Restaurant.objects.filter(owner=pk)
        serializer = ReadRestaurantSerializer(owner_resto, many=True)
        return Response(serializer.data)

