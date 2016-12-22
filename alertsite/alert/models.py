# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    event_time = models.DateTimeField()
    participants = models.ManyToManyField(User)
    place = models.CharField(max_length=50, blank=True)
    host = models.ForeignKey(User, related_name='event_host')
    invite_list = models.ManyToManyField(
        User,
        blank=True,
        related_name='invite_to_event'
    )
    active = models.BooleanField(default=True)

    def is_active(self):
        if self.event_time < timezone.now():
            return False
        else:
            return True

    def __unicode__(self):
        return self.title
