from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models


class Player(User):
    # implement
    # profile as foreignkey, about as charfield, player as manytomanyfield through friends model.
    friends = models.ManyToManyField('Player', through='friends.Friendship', verbose_name='list of friends')
    # rooms = models.ManyToManyField('self', through='chat.Room', verbose_name='list of rooms', symmetrical=False)

    def __unicode__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('accounts:profile', kwargs={'username': self.username})

    def get_friends_count(self):
        return self.friends.count()

    class Meta:
        app_label = 'accounts'
