from rest_framework import serializers
from .models import Dish, DishImage, Cuisine
from restaur.models import Restaurant



class WriteCuisineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuisine
        fields = ("name", "restaurant")

class ReadCuisineSerializer(serializers.ModelSerializer):
    restaurant = serializers.SlugRelatedField(slug_field="name", queryset=Restaurant.objects.all())
    class Meta:
        model = Cuisine
        fields = ("id", "name", "restaurant")



class WriteDishSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dish
        fields = ("name", "thumbnail", "restaurant", "cuisine", "duration", "description", "price")


class ReadDishSerializer(serializers.ModelSerializer):
    cuisine = serializers.SlugRelatedField(slug_field="name", queryset=Cuisine.objects.all())

    class Meta:
        model = Dish
        fields = ("id", "name", "thumbnail", "cuisine", "duration", "description", "price")
        

class WriteDishImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = DishImage
        fields = ("image", "dish")


class ReadDishImageSerializer(serializers.ModelSerializer):
    dish = serializers.SlugRelatedField(slug_field="name", queryset=Dish.objects.all())
    class Meta:
        model = DishImage
        fields = ("id", "image", "dish")
