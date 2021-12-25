from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Province(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="provinces")
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']

class District(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="districts")
    name = models.CharField(max_length=50, unique=True)
    province = models.ForeignKey(Province, on_delete=models.SET_NULL,
                                 null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']


class Sector(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sectors")
    name = models.CharField(max_length=50, unique=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL,
                                 null=True)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']
