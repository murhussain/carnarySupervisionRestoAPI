from rest_framework import serializers
from .models import Dish, Ingredient, DishImage, Cuisine
from restaur.models import Restaurant


class WriteIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ("name",)


class ReadIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ("id", "name")


class WriteCuisineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuisine
        fields = ("name", "restaurant")

class ReadCuisineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuisine
        fields = ("id", "name", "restaurant")

class WriteDishImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = DishImage
        fields = ("image")


class ReadDishImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishImage
        fields = str("image")


class WriteDishSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dish
        fields = ("thumbnail", "name", "restaurant", "cuisine", "duration", "price", "ingredient", "image")
        # depth = 1


class ReadDishSerializer(serializers.ModelSerializer):
    ingredient = serializers.SlugRelatedField(slug_field="name", queryset=Ingredient.objects.all(), many=True)
    # image = serializers.SlugRelatedField(slug_field="image", queryset=DishImage.objects.all(), many=True)

    class Meta:
        model = Dish
        fields = ("id", "thumbnail", "name", "cuisine", "restaurant", "duration", "price", "ingredient")
        

