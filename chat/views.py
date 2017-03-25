from django.db.models import Q
from django.views.generic import ListView
from .models import Room
from accounts.mixins import LoginRequiredMixin


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

