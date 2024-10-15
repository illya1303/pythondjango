from django.db import models


class Categorie(models.Model):
    name = models.CharField(max_length=20)


class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=9)
    counter = models.PositiveIntegerField(default=0)
    categories = models.ForeignKey(to=Categorie, on_delete=models.CASCADE)
