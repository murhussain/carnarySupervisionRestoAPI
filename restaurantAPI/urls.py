from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from restaur import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', include('location.urls')),
    path('catalog/', include('restaur.urls')),
    path('favourite/', views.FavRestaurants, name="favResto"),
    path('kitchen/', include('dishes.urls')),
    path('login/', obtain_auth_token, name="obtain-auth-token"),
    path('admin/', admin.site.urls),
    path('login/', obtain_auth_token , name="obtain-auth-token"),
    path('api-auth/', include('rest_framework.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)