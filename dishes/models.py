from django.contrib.auth.models import User
from django.db import models
from restaur.models import Restaurant
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Ingredient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ingredients")
    name = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name


def uploadTo(instance, filename):
    return 'dishes/{filename}'.format(filename=filename)


class DishImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="dishimages")
    image = models.ImageField(
        _("image"), upload_to=uploadTo, default='dishes/default.png')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.image)

    class Meta:
        ordering = ['-created_at']


class Cuisine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cuisines")
    name = models.CharField(max_length=50, blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="cuisines")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']


class Dish(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="dishes")
    name = models.CharField(max_length=80, blank=True)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE, default=1, related_name="cuisines")
    duration = models.DurationField()
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
