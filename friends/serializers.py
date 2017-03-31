from rest_framework import serializers

from .models import *
from accounts.serializers import PlayerDetailSerializer


class FriendshipDetailSerializer(serializers.ModelSerializer):
    player1 = PlayerDetailSerializer()
    player2 = PlayerDetailSerializer()

    class Meta:
        model = Friendship

        fields = [
            "player1",
            "player2",
            "player1_approve",
            "player2_approve"
        ]
