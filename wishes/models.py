from django.db import models


class wishesCategory(models.Model):
    cat_name = models.TextField(max_length=100)
    cat_img = models.FileField(upload_to='wishesImg/', blank=True)
    cat_des = models.TextField()

class wishes(models.Model):
    cat = models.ForeignKey(wishesCategory,on_delete=models.CASCADE)
    wish = models.TextField()
    datetime = models.DateTimeField(auto_now=True)
    subcategory = models.TextField(max_length=50)

