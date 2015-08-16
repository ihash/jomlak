from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    text = models.TextField()
    likes = models.IntegerField(default=0)
    # user = models.ForeignKey(to=User)

    def __str__(self):
        return self.text

    @property
    def get_url(self):
        return '/like/{}/'.format(self.id)