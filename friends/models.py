from __future__ import unicode_literals

from django.db import models


class Friendship(models.Model):
    player1 = models.ForeignKey('accounts.Player', related_name='player1', on_delete=models.CASCADE)
    player2 = models.ForeignKey('accounts.Player', related_name='player2', on_delete=models.CASCADE)

    player1_approve = models.BooleanField(default=False)
    player2_approve = models.BooleanField(default=False)

    requested_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)

    room_created = models.BooleanField(default=False)  # make True when friend request accepted

    def __unicode__(self):
        return "%s - %s - %s" % (self.player1.username, self.player2.username, str(self.requested_at))

    class Meta:
        app_label = 'friends'
