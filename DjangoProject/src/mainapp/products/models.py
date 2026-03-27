from django.db import models

# Create your models here.

PRODUCT_CHOICES = {
    ("appetizers","appetizers"),
    ("entrees","entrees"),
    ("treats","treats"),
    ("drinks","drinks"),
}

class Product(models.Model):
    type = models.CharField(max_length=60, choices=PRODUCT_CHOICES)
    name = models.CharField(max_length=60, default = "", blank = True, null = False)
    description = models.TextField(max_length=300, default="", blank = True)
    price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    image = models.CharField(max_length=255, default="temporary/path", blank=True)

    objects = models.Manager()
    
    def __str__(self):
        return self.name
