from django.conf import settings
from django.contrib import admin
from django.db import models

# Create your models here.
from django.http import request
from django.utils import timezone


class TweetStatus(models.TextChoices):
    PENDING = 'PE', 'Pending'
    COMPLETED = 'CO', 'Completed'
    DROPPED = 'DR', 'Dropped'
class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Tweet(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now())
    completed_at= models.DateTimeField(null=True)
    deadline = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=2, choices=TweetStatus.choices, default=TweetStatus.PENDING)
    tweeted_by =  models.TextField(null= True)
    tags = models.ManyToManyField(Tag, null=True, blank=True)

    '''
    @property
    def foo(self):
        return 'hello'
    '''
    def __str__(self):
        return f'{self.content} - {self.status}'
    def get_all_tags(self, delimiter= ' ,'):
        return delimiter.join([tag.name for tag in self.tags.all()])


