from django.db import models
from datetime import datetime
from tenants.models import Tenant

class Listing(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    zipcode = models.CharField(max_length=16)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    kitchen = models.IntegerField()
    garage = models.BooleanField(null=True)
    sqft = models.IntegerField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
    
