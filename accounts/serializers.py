from rest_framework import serializers

from accounts.models import *


class PlayerDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = [
            "username"
        ]
