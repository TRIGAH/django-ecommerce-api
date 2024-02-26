from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = TreeForeignKey("self", on_delete=models.PROTECT,blank=True,null=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)
 
    def __str__(self):
        return self.name   



class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100,blank=True)
    is_digital = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = TreeForeignKey("Category",blank=True,null=True)
 
    def __str__(self):
        return self.name   
    

