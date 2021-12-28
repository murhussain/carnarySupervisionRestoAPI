from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from location.models import District, Sector


def upload_to(instance, filename):
    return 'resto/{filename}'.format(filename=filename)


# Create your models here.
class Owner(models.Model):
    class OwnerType(models.TextChoices):
        INDIVIDUAL = 'Individual'
        COMPANY = 'Company'
    name = models.CharField(max_length=100, default="SomeOne")
    type = models.CharField(max_length=30, choices=OwnerType.choices, default=OwnerType.INDIVIDUAL)

    def __str__(self):
        return f'{self.name}, {self.type}'


class Restaurant(models.Model):
    name = models.CharField(max_length=50, blank=True)
    image = models.ImageField(
        _("image"), upload_to=upload_to)
    owner = models.ForeignKey(Owner, on_delete=models.SET_NULL,
                              related_name="owners", null=True)
    rating = models.IntegerField(default=0,
                                 validators=[
                                     MaxValueValidator(5),
                                     MinValueValidator(0),
                                 ], )
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name="restaurants")
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE, related_name="restaurants")
    created_at = models.DateTimeField(auto_now_add=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="restaurants")

    def __str__(self):
        return f'{self.name}, {self.district.name}'

    class Meta:
        ordering = ['-created_at']
