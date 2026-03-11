from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    GENRE_CHOICES = [
        (1, 'History'),
        (2, 'Sci-Fi'),
        (3, 'Romance'),
        (4, 'Thriller'),
        (5, 'Fantasy')
    ]

    name = models.IntegerField(choices=GENRE_CHOICES, default=1)
    description = models.TextField()
    is_popular = models.BooleanField(default=True)

class Author(models.Model):
    EXPERIENCE_CHOICES = [
        (1, 'Beginner'),
        (2, 'Professional'),
        (3, 'Established')
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    biography = models.TextField()
    experience_level = models.IntegerField(choices=EXPERIENCE_CHOICES, default=1)

class Book(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField()
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(to=Genre, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to='book_images/')
    rental_price = models.IntegerField(default=0)
    available_copies = models.IntegerField(default=0)