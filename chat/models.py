import json
from django.db import models
from channels import Group

from .settings import MSG_TYPE_MESSAGE


class RoomManager(models.Manager):
    def create_room(self):  # call this function when friend request accepted
        room = self.create()
        return room


class Room(models.Model):  # a room for friends to chat in

    room = models.OneToOneField('friends.Friendship', on_delete=models.CASCADE, primary_key=True)
    message = models.TextField(blank=True, null=True)
    last_used = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "Room of %s and %s" % (self.room.player1.username, self.room.player2.username)

    @property
    def websocket_group(self):
        """
        Returns the Channels Group that sockets should subscribe to to get sent
        messages as they are generated.
        """
        return Group("room-%s" % self.id)

    def send_message(self, message, user, msg_type=MSG_TYPE_MESSAGE):
        """
        Called to send a message to the room on behalf of a user.
        """
        final_msg = {'room': str(self.id), 'message': message, 'username': user.username, 'msg_type': msg_type}

        # Send out the message to everyone in the room
        self.websocket_group.send(
            {"text": json.dumps(final_msg)}
        )


