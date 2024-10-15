from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=20)


class Products(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=9)
    counter = models.PositiveIntegerField(default=0)
    categories = models.ForeignKey(to=Categories, on_delete=models.CASCADE)
