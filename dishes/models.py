from django.db import models
from restaur.models import Restaurant
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name


def uploadTo(instance, filename):
    return 'dishes/{filename}'.format(filename=filename)

class DishImage(models.Model):
    image = models.ImageField(
        _("image"), upload_to=uploadTo)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.image)

    class Meta:
        ordering = ['-created_at']


class Cuisine(models.Model):
    name = models.CharField(max_length=50, blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="cuisines")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']


def uploadThumbnail(instance, filename):
    return 'thumbnail/{filename}'.format(filename=filename)


class Dish(models.Model):
    name = models.CharField(max_length=80, blank=True)
    thumbnail = models.ImageField(
        _("image"), upload_to=uploadThumbnail)
    homeImage = models.ImageField(("image"), upload_to=uploadThumbnail, null=True)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE, default=1, related_name="cuisines")
    duration = models.DurationField()
    description = models.TextField(default="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,")
    ingredient = models.ManyToManyField(Ingredient)
    image = models.ManyToManyField(DishImage)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL,
                                   related_name="restaurants", null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
