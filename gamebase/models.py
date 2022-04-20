from lib2to3.pgen2.pgen import generate_grammar
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Game(models.Model):
    game_id = models.IntegerField(primary_key=True, default=0)
    name = models.CharField(max_length=250)
    official_trailer = models.TextField(blank = True, null = True)
    main_picture = models.CharField(max_length=250, blank = True, null = True)
    release_date = models.CharField(max_length=50, blank = True, null = True)
    description = models.TextField(blank = True, null = True)
    cover_photo = models.CharField(max_length=250, blank = True, null = True)
    average_rating = models.FloatField(max_length=100, blank = True, null = True)
    company_names = models.TextField(blank = True, null = True)
    website = models.TextField(blank = True, null = True)

    def _str_(self):
        return self.name


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    comment = models.TextField()
    time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["time"]