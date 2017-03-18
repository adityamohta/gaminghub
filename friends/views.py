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

    # custom method to get player instance from user object.
    def get_player_instance(self):
        try:
            player = Player.objects.get(id=self.request.user.id)
        except:
            raise Http404
        return player

    def get_context_data(self, *args, **kwargs):
        player = self.get_player_instance()
        # friend requests sent
        frs_qs = Friendship.objects.filter(
                (Q(player1=player) & (Q(player1_approve=True) & Q(player2_approve=False))) |
                (Q(player2=player) & (Q(player1_approve=False) & Q(player2_approve=True)))
        )

        # friend requests received
        frr_qs = Friendship.objects.filter(
                (Q(player1=player) & (Q(player1_approve=False) & Q(player2_approve=True))) |
                (Q(player2=player) & (Q(player1_approve=True) & Q(player2_approve=False)))
        )
        frs_id_list = []
        frr_id_list = []

        for obj in frs_qs:
            frs_id_list.append(obj.player1.id if obj.player1 != player else obj.player2.id)
        for obj in frr_qs:
            frr_id_list.append(obj.player1.id if obj.player1 != player else obj.player2.id)

        frs_list = Player.objects.filter(pk__in=frs_id_list)
        frr_list = Player.objects.filter(pk__in=frr_id_list)

        context = super(FriendList, self).get_context_data(*args, **kwargs)
        context["friend_requests_sent"] = frs_list
        context["friend_requests_received"] = frr_list
        return context

    def get_queryset(self):
        player = self.get_player_instance()
        qs = Friendship.objects.filter(
                (Q(player1=player) | Q(player2=player)) &
                (Q(player1_approve=True) & Q(player2_approve=True))
        )

        player_id_list = []

        for obj in qs:
            player_id_list.append(obj.player1.id if obj.player1 != player else obj.player2.id)

        friend_list = Player.objects.filter(pk__in=player_id_list)

        # print(qs)
        # print(friend_list)
        # print(player.username)
        return friend_list
