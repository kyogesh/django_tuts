import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class PollUser(User):

    def __unicode__(self):
        return self.username


class Poll(models.Model):

    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    created_by = models.ForeignKey(PollUser)

    def was_published_recently(self):
        return self.pub_date > (timezone.now() - datetime.timedelta(days=1))

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published Recently?'

    def __unicode__(self):
        return self.question


class Choice(models.Model):

    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice
