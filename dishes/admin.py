from django.contrib import admin
from .models import Dish, DishImage, Cuisine

# Register your models here.
admin.site.register(Dish)
admin.site.register(DishImage)
admin.site.register(Cuisine)