from django.db import models

class myfeelings(models.Model):
    feeling = models.TextField()
    datetime = models.DateTimeField(auto_now=True)
    mood = models.TextField(max_length=50)
