from django.db import models
from django.conf import settings

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rating = models.PositiveSmallIntegerField(default=0)

class UserBook(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    is_favorite = models.BooleanField(default=False)
    is_reading = models.BooleanField(default=False)
    is_read = models.BooleanField(default=False)
    rating = models.PositiveSmallIntegerField(default=0)
