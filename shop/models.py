from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Products(models.Model):
    title = models.CharField(max_length =200)
    price = models.FloatField()
    discount_price = models.FloatField()
    categorie = models.CharField(max_length=200)
    image = models.CharField(max_length=300)
    description = models.TextField()





