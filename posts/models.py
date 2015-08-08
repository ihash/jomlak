from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    text = models.TextField()
    likes = models.IntegerField(default=0)
    # user = models.ForeignKey(to=User)


    # quote = models.CharField('public quote', max_length=160)