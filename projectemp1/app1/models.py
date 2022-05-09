from django.db import models

# Create your models here.
class Employee(models.Model):
    eid = models.IntegerField()
    ename = models.CharField(max_length=100)
    eadd = models.CharField(max_length=500)
    esal = models.FloatField()
    email = models.EmailField(default='som@gamil.com')

    def __str__(self):
        return self.ename
