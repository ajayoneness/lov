from django.db import models

class yourfeelings(models.Model):
    name = models.TextField()
    yourfeeling = models.TextField()
    datetime = models.DateTimeField(auto_now=True)
    your_mood = models.TextField(max_length=50)
