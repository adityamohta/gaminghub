from django.db.models import Q
from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

from rest_framework.generics import RetrieveAPIView, ListAPIView

from .models import Room
from accounts.mixins import LoginRequiredMixin
from accounts.models import Player
from chat.serializers import *


class RoomDetailView(LoginRequiredMixin, DetailView):
    model = Room
    context_object_name = "room"
    template_name = "chat/room.html"

    def get_object(self, *args):
        try:
            player = get_object_or_404(Player, id=self.request.user.id)
            friend_username = self.kwargs["username"]
            rooms = Room.objects.filter(
                (Q(friendship__player1__username=player) | Q(friendship__player2__username=player)) &
                (Q(friendship__player1__username=friend_username) | Q(friendship__player2__username=friend_username))
            )
            if not rooms.exists():
                raise Http404
            room = rooms.first()
            return room
        except:
            raise Http404


class RoomList(LoginRequiredMixin, ListView):
    model = Room
    template_name = 'chat/index.html'
    context_object_name = "rooms"

    def get_queryset(self):
        current_user = self.request.user
        rooms = Room.objects.filter(
            Q(friendship__player1__username=current_user) |
            Q(friendship__player2__username=current_user)
        )
        return rooms


class RoomListApiView(ListAPIView):
    serializer_class = RoomListSerializer
    def get_queryset(self):
        username = self.request.user.username
        rooms = Room.objects.filter(
                Q(friendship__player1__username=username) |
                Q(friendship__player2__username=username)
        )
        return rooms


class RoomMessageListAPIView(RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomDetailSerializer
    lookup_field = "pk"
