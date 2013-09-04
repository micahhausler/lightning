from django.db import models


class Album(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField()
    summary = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    is_live = models.BooleanField()


class Photo(models.Model):
    title = models.CharField(max_length=256)
    summary = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='photos/%Y/%m')
    album = models.ForeignKey(Album)
    is_live = models.BooleanField()
