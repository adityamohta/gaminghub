import json
from django.db import models
from channels import Group

from .settings import MSG_TYPE_MESSAGE


class RoomManager(models.Manager):
    def create_room(self):  # call this function when friend request accepted
        room = self.create()
        return room


class Message(models.Model):
    user = models.ForeignKey("accounts.Player", related_name="messages", null=True, blank=True)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey("Room", related_name="messages")


class Room(models.Model):  # a room for friends to chat in

    friendship = models.OneToOneField('friends.Friendship', on_delete=models.CASCADE, primary_key=True)
    # message = models.TextField(blank=True, null=True)
    last_used = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "Room of %s and %s" % (self.friendship.player1.username, self.friendship.player2.username)

    @property
    def websocket_group(self):
        """
        Returns the Channels Group that sockets should subscribe to to get sent
        messages as they are generated.
        """
        return Group("room-%s" % self.friendship.id)

    def send_message(self, message, user, msg_type=MSG_TYPE_MESSAGE):
        """
        Called to send a message to the room on behalf of a user.
        """
        final_msg = {'room': str(self.friendship.id), 'message': message, 'username': user.username, 'msg_type': msg_type}
        self.save()
        print(message)
        # Send out the message to everyone in the room
        self.websocket_group.send(
            {"text": json.dumps(final_msg)}
        )


