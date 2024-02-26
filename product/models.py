from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    pass


class Brand(models.Model):
    name = models.CharField(max_length=100)
    pass


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100,blank=True)
    is_digital = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    

