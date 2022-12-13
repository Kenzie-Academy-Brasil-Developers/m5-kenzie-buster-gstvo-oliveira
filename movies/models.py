from django.db import models
from users.models import User


class CategoryRating(models.TextChoices):
    G = 'G'
    PG = 'PG'
    PG_13 = 'PG_13'
    R = 'R'
    NC_17 = 'NC_17'


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True)
    rating = models.CharField(max_length=20, choices=CategoryRating.choices, default=CategoryRating.G)
    synopsis = models.TextField(null=True)


    user = models.ForeignKey(
        'users.User', on_delete=models.CASCADE, related_name='movies'
    )

    user_buy = models.ManyToManyField(
        User, through='MovieOrder', related_name='movies_bought'
    )


class MovieOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    buyed_at = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)