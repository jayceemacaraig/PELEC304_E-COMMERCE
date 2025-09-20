from django.db import models

# Create your models here.
class Product(models.Model):
    item_name = models.CharField(max_length=100)
    product_category = models.CharField(max_length=100)
    description = models.CharField()
    price = models.FloatField()
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_name
    

class NewRelease(models.Model):
    item_name = models.CharField(max_length=100)
    product_category = models.CharField(max_length=100)
    description = models.CharField()
    price = models.FloatField()
    image = models.ImageField(upload_to='new_release/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_name
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='category/')

    def __str__(self):
        return self.name