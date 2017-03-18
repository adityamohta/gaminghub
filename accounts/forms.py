from django import forms
from django.contrib.auth import authenticate

from accounts.models import Player


class PlayerCreateForm(forms.ModelForm):
    # customize it futher here.
    # add password and email verification, validation here.
    # user widgets to add classes of materialize.css framework.
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Password must match!")
        if not 8 < len(str(password)) < 30:
            raise forms.ValidationError("Password's length must be in between 8 to 30 characters.")
        return password

    def save(self, commit=True):
        player = super(PlayerCreateForm, self).save(commit=False)
        password = player.password
        player.set_password(password)
        if commit:
            player.save()
        return player

    class Meta:
        model = Player
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
            "confirm_password"
        ]


class PlayerUpdateForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = [
            "first_name",
            "last_name"
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
