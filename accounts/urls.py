from django.conf.urls import url

from accounts.views import (
    PlayerCreate,
    PlayerDetail,
    PlayerList,
    PlayerLogin,
    PlayerLogout
)

urlpatterns = [
    url(r"^$", PlayerList.as_view(), name="players"),
    url(r"^login/$", PlayerLogin.as_view(), name="login"),
    url(r"^logout/$", PlayerLogout.as_view(), name="logout"),
    url(r"^create/$", PlayerCreate.as_view(), name="create"),
    url(r"^(?P<username>[\w.@+-]+)/profile/$", PlayerDetail.as_view(), name="profile"),
]
