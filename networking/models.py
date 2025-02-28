from django.db import models

# Create your models here.
class Networking(models.Model):
    item_image = models.ImageField(default="default.jpeg")
    title = models.CharField(max_length=100, default="Adds")
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
class Items(models.Model):
    image = models.ImageField(default="default.jpeg")
    title = models.CharField(max_length=100, default='Ads')
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.title