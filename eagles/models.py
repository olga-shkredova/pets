from django.db import models


class Eagles(models.Model):
    title = models.CharField(max_length=150)
    species = models.CharField(max_length=100)
    description = models.TextField()
    image = models.FileField(upload_to='image/')
