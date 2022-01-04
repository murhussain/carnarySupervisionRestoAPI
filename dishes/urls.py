from django.urls import path
from dishes.views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"cuisine", CuisineModelViewSet, basename="cuisine")
router.register(r"dish", DishModelViewSet, basename="dishes")
router.register(r"dishImage", DishImageModelViewSet, basename="dishImage")
urlpatterns = [
]
urlpatterns += router.urls