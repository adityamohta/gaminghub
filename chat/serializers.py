from rest_framework import serializers

from chat.models import *


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message

        fields = [
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
