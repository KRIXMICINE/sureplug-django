from django.db import models
from django.urls import reverse
from category.models import category

# Create your models here.

class product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200)
    description = models.TextField(max_length=250, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='photos/product')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    # rating = models.IntegerField
    
    
    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])
    
    
    def __str__(self):
        return self.product_name
    