from rest_framework import serializers
from .models import *


class WriteOwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Owner
        fields = ("name", "type")


class ReadOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ("id", "name", "type")


class WriteRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ("name", "image", "owner", "rating", "district", "sector")


class ReadRestaurantSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(slug_field="name", queryset=Owner.objects.all())
    # district = serializers.SlugRelatedField(slug_field="name", queryset=District.objects.all())
    # sector = serializers.SlugRelatedField(slug_field="name", queryset=Sector.objects.all())

    class Meta:
        model = Restaurant
        fields = ("id", "name", "image", "owner", "rating", "district", "sector")
        # depth = 1
        # read_only_fields = fields
