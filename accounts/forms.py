from django import forms

from accounts.models import Player


class PlayerCreateForm(forms.ModelForm):
    # customize it futher here.
    # add password and email verification, validation here.
    # user widgets to add classes of materialize.css framework.

    class Meta:
        model = Player
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password"
        ]
