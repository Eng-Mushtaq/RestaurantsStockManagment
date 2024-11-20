from django.db import models

# Create your models here.
# Categories Model
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    

 # Categories Model 
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name
