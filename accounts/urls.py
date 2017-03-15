from django.conf.urls import url

from accounts.views import PlayerCreate, PlayerDetail, PlayerList

urlpatterns = [
    url(r"^$", PlayerList.as_view(), name="players"),
    url(r"^create/$", PlayerCreate.as_view(), name="create"),
    url(r"^(?P<username>[\w.@+-]+)/profile/$", PlayerDetail.as_view(), name="profile"),
]
