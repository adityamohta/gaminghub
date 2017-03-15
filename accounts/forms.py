from django import forms
from django.contrib.auth import authenticate

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


class PlayerLoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)

            if not user:
                raise forms.ValidationError("This user doesn't exist!")

        return super(PlayerLoginForm, self).clean(*args, **kwargs)
