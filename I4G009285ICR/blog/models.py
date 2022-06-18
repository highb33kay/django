from cgitb import text
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    text = models.TextField()
    author = models.ForeignKey(get_user_model(), null=True, on_delete=models.PROTECT)
    created_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)

