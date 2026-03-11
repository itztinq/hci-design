from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import TextField, BooleanField, CharField


class Category(models.Model):
    CATEGORY_NAME = [
        (1, 'Cardio'),
        (2, 'Yoga'),
        (3, 'Strength')
    ]

    name = models.IntegerField(choices=CATEGORY_NAME, default=1)
    description = TextField()
    is_in_high_demand = BooleanField(default=False)

class Instructor(models.Model):
    EXPERIENCE = [
        (1, 'Beginner'),
        (2, 'Certified'),
        (3, 'Professional')
    ]

    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    biography = TextField()
    experience_level = models.IntegerField(choices=EXPERIENCE, default=1)

class Training(models.Model):
    name = models.CharField(max_length=100)
    instructor = models.ForeignKey(to=Instructor, on_delete=models.CASCADE)
    description = models.TextField()
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    price_per_session = models.IntegerField(default=0)
    available_spots = models.IntegerField(default=0)