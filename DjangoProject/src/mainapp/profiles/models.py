from django.db import models

# Create your models here.

TITLE_CHOICES = {
    ("Mr.", "Mr."),
    ("Mrs.", "Mrs."),
    ("Ms.", "Ms."),
    
}


class Profile(models.Model):
    title = models.CharField(default="", choices=TITLE_CHOICES)
    first_name = models.CharField(max_length=50, blank=True, default="")
    last_name = models.CharField(max_length=50, blank=True, default="")
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=150, unique=True)

    objects = models.Manager()

    def __str__(self):
        return self.username
    
    

    