from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models


# Create your models here.


class Player(User):
    # implement
    # profile as foreignkey, about as charfield, player as manytomanyfield through friends model.

    def get_absolute_url(self):
        return reverse('accounts:profile', kwargs={'username': self.username})

    class Meta:
        app_label = "accounts"
