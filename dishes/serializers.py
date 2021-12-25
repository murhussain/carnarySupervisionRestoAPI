from rest_framework import serializers
from .models import Dish, Ingredient, DishImage, Cuisine


class WriteIngredientSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Ingredient
        fields = ( "user", "name")


class ReadIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ("id", "name")


class WriteCuisineSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Cuisine
        fields = ("user", "name", "restaurant")

class ReadCuisineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuisine
        fields = ("id", "name")

class WriteDishImageSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = DishImage
        fields = ( "user", "image")


class ReadDishImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishImage
        fields = str("__all__")


class WriteDishSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Dish
        fields = ("user", "name", "cuisine", "duration", "price", "ingredient", "image")
        # depth = 1


class ReadDishSerializer(serializers.ModelSerializer):
    cuisine = serializers.SlugRelatedField(slug_field="name", queryset=Cuisine.objects.all())
    ingredient = serializers.SlugRelatedField(slug_field="name", queryset=Ingredient.objects.all(), many=True)
    image = ReadDishImageSerializer(many=True)

    class Meta:
        model = Dish
        fields = ("id", "name", "cuisine", "duration", "price", "ingredient", "image")
        # depth = 3
        read_only_fields = fields
