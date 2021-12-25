from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from restaur.models import Restaurant
from restaur.serializers import *
from .models import District, Sector
from .permissions import IsAdminOrReadOnly
from .serializers import *


# Create your views here.
class ProvinceModelViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name"]

    def get_queryset(self):
        return Province.objects.all()

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return ReadProvinceSerializer
        return WriteProvinceSerializer

    @action(detail=True, methods=['get'])
    def districts(self, request, pk=None):
        prov_dist = District.objects.filter(province=pk)
        serializer = ReadDistrictSerializer(prov_dist, many=True)
        return Response(serializer.data)



class DistrictModelViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name"]

    def get_queryset(self):
        return District.objects.all()

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return ReadDistrictSerializer
        return WriteDistrictSerializer

    @action(detail=True, methods=['get'])
    def restaurants(self, request, pk=None):
        dist_resto = Restaurant.objects.filter(district=pk)
        serializer = ReadRestaurantSerializer(dist_resto, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def sectors(self, request, pk=None):
        dist_sect = Sector.objects.filter(district=pk)
        serializer = ReadSectorSerializer(dist_sect, many=True)
        return Response(serializer.data)


class SectorModelViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name"]

    def get_queryset(self):
        return Sector.objects.select_related("district", "user")

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return ReadSectorSerializer
        return WriteSectorSerializer

    @action(detail=True, methods=['get'])
    def restaurants(self, request, pk=None):
        sect_resto = Restaurant.objects.filter(sector=pk)
        serializer = ReadRestaurantSerializer(sect_resto, many=True)
        return Response(serializer.data)