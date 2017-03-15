from django.http import Http404
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView

from accounts.forms import PlayerCreateForm
from accounts.models import Player


class PlayerDetail(DetailView):
    model = Player
    context_object_name = "player"
    # template_name = "accounts/player_detail.html"     # this is default value of template_name

    def get_object(self, *args):
        try:
            player = Player.objects.get(username=self.kwargs["username"])
            return player
        except:
            raise Http404


class PlayerList(ListView):
    model = Player
    context_object_name = "players"
    # template_name = "accounts/player_list.html"     # this is default value of template_name


class PlayerCreate(CreateView):     # create view/ registration
    model = Player
    context_object_name = "form"
    form_class = PlayerCreateForm
    # in CreateView default template name is "<app_name>/<model_name>_form"
    # therefore in this case default name was "accounts/player_form.html"
    template_name = "accounts/player_create.html"
