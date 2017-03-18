from django.contrib.auth import authenticate, login, logout
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import (
    CreateView,
    DetailView,
    FormView,
    ListView,
    UpdateView
)
from django.views import View

from accounts.forms import PlayerCreateForm, PlayerLoginForm, PlayerUpdateForm
from accounts.models import Player
from accounts.mixins import LoginRequiredMixin


class PlayerDetail(LoginRequiredMixin, DetailView):
    model = Player
    context_object_name = "player"
    # template_name = "accounts/player_detail.html"     # this is default value of template_name

    def get_object(self, *args):
        try:
            player = Player.objects.get(username=self.kwargs["username"])
            return player
        except:
            raise Http404


class PlayerList(LoginRequiredMixin, ListView):
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

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect("accounts:players")
        return super(PlayerCreate, self).get(request, *args, **kwargs)


class PlayerLogin(FormView):
    form_class = PlayerLoginForm
    template_name = "accounts/player_login.html"
    success_url = "/accounts/"

    def get_player_instance(self, user_id):
        try:
            player = Player.objects.get(id=user_id)
        except:
            raise Http404
        return player

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect("accounts:players")
        return super(PlayerLogin, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(self.request, user)
        player = self.get_player_instance(user.id)
        # session variables accessed in navbar.
        self.request.session["name"] = player.get_full_name()
        self.request.session["username"] = player.username
        self.request.session["email"] = player.email
        return super(PlayerLogin, self).form_valid(form)


class PlayerLogout(View):

    def get(self, request, *args, **kwargs):
        # if not request.user.is_authenticated():
        #     raise Http404
        # optional - add message
        logout(request)
        return redirect("accounts:login")


class PlayerUpdate(LoginRequiredMixin, UpdateView):
    model = Player
    form_class = PlayerUpdateForm
    template_name = "accounts/player_update.html"

    def get_player_instance(self):
        try:
            player = Player.objects.get(id=self.request.user.id)
        except:
            raise Http404
        return player

    def get_object(self, queryset=None):
        return self.get_player_instance()

    def form_valid(self, form):
        first_name = form.cleaned_data.get("first_name")
        last_name = form.cleaned_data.get("last_name")

        self.request.session["name"] = "%s %s" % (first_name, last_name)
        return super(PlayerUpdate, self).form_valid(form)
