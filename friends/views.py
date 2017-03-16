from django.db.models import Q
from django.http import Http404
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from accounts.mixins import LoginRequiredMixin
from accounts.models import Player
from friends.models import Friendship


class FriendList(LoginRequiredMixin, ListView):
    model = Friendship
    context_object_name = "friends"
    template_name = "friends/friend_list.html"

    def get_queryset(self):
        try:
            player = Player.objects.get(id=self.request.user.id)
        except:
            raise Http404
        qs = Friendship.objects.filter(
                (Q(player1=player) | Q(player2=player)) &
                (Q(player1_approve=True) & Q(player2_approve=True))
        )
        player_id_list = []
        for obj in qs:
            player_id_list.append(obj.player1.id if obj.player1 != player else obj.player2.id)

        friend_list = Player.objects.filter(pk__in=player_id_list)
        print(qs)
        print(friend_list)
        print(player.username)
        return friend_list

