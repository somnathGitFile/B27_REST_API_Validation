from django.db import models

# Create your models here.
class Customer(models.Model):
    cid = models.IntegerField()
    cname = models.CharField(max_length=100)
    cadd = models.CharField(max_length=100)
    cmail = models.EmailField(default='umesh@gmail.com')
    cpay = models.FloatField()