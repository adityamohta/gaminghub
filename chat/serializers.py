from rest_framework import serializers

from accounts.serializers import PlayerDetailSerializer
from friends.serializers import FriendshipDetailSerializer
from chat.models import *


class MessageSerializer(serializers.ModelSerializer):
    user = PlayerDetailSerializer()

    class Meta:
        model = Message

        fields = [
            "user",
            "text",
            "timestamp",
            "room_id",
        ]


class RoomDetailSerializer(serializers.ModelSerializer):
    messages = serializers.SerializerMethodField()

    def get_messages(self, obj):
        msgs = obj.messages.all().order_by("timestamp")
        serialized_messages = MessageSerializer(msgs, many=True)
        return serialized_messages.data

    class Meta:
        model = Room

        fields = [
            "messages"
        ]


class RoomListSerializer(serializers.ModelSerializer):
    messages = serializers.SerializerMethodField()
    friendship = FriendshipDetailSerializer()

    def get_messages(self, obj):
        msgs = obj.messages.all().order_by("timestamp")
        serialized_messages = MessageSerializer(msgs, many=True)
        return serialized_messages.data

    class Meta:
        model = Room

        fields = [
            "friendship",
            "messages",
        ]
