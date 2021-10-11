from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='portfolio/images')
    url = models.URLField(blank=True)
    date = models.DateField()
    body = models.TextField()
