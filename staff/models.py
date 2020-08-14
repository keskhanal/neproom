from django.db import models

class Staff(models.Model):
    name = models.CharField(max_length=64)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    phone = models.CharField(max_length=16)
    email = models.CharField(max_length=20)

    def __str__(self):
        return self.name