from django.db import models

class ProductionCompany(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    year_of_foundation = models.IntegerField()
    website = models.URLField()

class Movie(models.Model):
    GENRE_CHOICES = [
        ('Action', 'Action'),
        ('Comedy', 'Comedy'),
        ('Drama', 'Drama'),
        ('Horror', 'Horror'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Documentary', 'Documentary'),
        ('Animation', 'Animation'),
    ]

    FORMAT_CHOICES = [
        ('Digital', 'Digital'),
        ('Blu-ray', 'Blu-ray'),
        ('DVD', 'DVD'),
    ]

    title = models.CharField(max_length=200)
    poster = models.ImageField(upload_to='posters/')
    imdb_code = models.CharField(max_length=20)
    year = models.IntegerField()
    production = models.ForeignKey(ProductionCompany, on_delete=models.CASCADE)
    duration = models.IntegerField()
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    format = models.CharField(max_length=20, choices=FORMAT_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)