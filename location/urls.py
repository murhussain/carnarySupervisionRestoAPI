from django.urls import path
from location.views import ProvinceModelViewSet, SectorModelViewSet, DistrictModelViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"province", ProvinceModelViewSet, basename="provinces")
router.register(r"district", DistrictModelViewSet, basename="districts")
router.register(r"sector", SectorModelViewSet, basename="sectors")
urlpatterns = [
]
urlpatterns += router.urls