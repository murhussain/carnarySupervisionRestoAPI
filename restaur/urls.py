from django.urls import path
from restaur.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"restaurant", RestaurantModelViewSet, basename="restaurants")
router.register(r"owner", OwnerModelViewSet, basename="owner")
urlpatterns = [
]
urlpatterns += router.urls
