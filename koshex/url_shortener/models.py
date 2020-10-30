from django.db import models

# Create your models here.

class Urls (models.Model):
    long_url = models.URLField(max_length = 1000)
    short_url = models.CharField(max_length = 12, unique = True)
    total_hits = models.IntegerField(default = 0)
    created_at = models.DateTimeField( auto_now_add = True)

    