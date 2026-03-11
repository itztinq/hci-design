from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    isActive = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Company(models.Model):
    class CompanyType(models.IntegerChoices):
        small = 1, 'small'
        medium = 2, 'medium'
        big = 3, 'big'

    name = models.CharField(max_length=100)
    foundationDate = models.DateField()
    type = models.IntegerField(choices=CompanyType, default=CompanyType.small)

    def __str__(self):
        return self.name

class Supplement(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(to=Company, on_delete=models.CASCADE)
    description = models.TextField()
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name