from django.db import models


class PhotoBlog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(default='gomimta.jpg')
