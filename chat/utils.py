from functools import wraps

from .exceptions import ClientError
from .models import Room
from accounts.models import Player


def catch_client_error(func):
    """
    Decorator to catch the ClientError exception and translate it into a reply.
    """
    @wraps(func)
    def inner(message, *args, **kwargs):
        try:
            return func(message, *args, **kwargs)
        except ClientError as e:
            # If we catch a client error, tell it to send an error string
            # back to the client on their reply channel
            e.send_to(message.reply_channel)
    return inner


def get_room_or_error(room_id, user):
    """
    Tries to fetch a room for the user, checking permissions along the way.
    """
    # Find the room they requested (by ID)
    try:
        room = Room.objects.get(pk=room_id)
    except Room.DoesNotExist:
        raise ClientError("ROOM_INVALID")
    return room


def get_player_or_error(user):
    try:
        player = Player.objects.get(id=user.id)
    except Player.DoesNotExist:
        raise ClientError("PLAYER_INVALID")
    return player
