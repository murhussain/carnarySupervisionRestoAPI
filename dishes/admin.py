from django.contrib import admin
from .models import Ingredient, Dish, DishImage, Cuisine

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(Dish)
admin.site.register(DishImage)
admin.site.register(Cuisine)