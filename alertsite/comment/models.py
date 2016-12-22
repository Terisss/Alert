from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from alert.models import Event
from django.utils import timezone
import datetime
# Create your models here.


class Comment(models.Model):
    body = models.TextField(max_length=2000)
    author = models.ForeignKey(User, blank=True)
    event = models.ForeignKey(Event)
    enable = models.BooleanField(default=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    patch_date = models.DateTimeField(auto_now=True)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(minutes=30) <= self.pub_date <= now

    def __unicode__(self):
        return "Comment to %s" % self.event.title
