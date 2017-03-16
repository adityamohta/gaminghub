from django.conf.urls import url

from friends.views import FriendList


urlpatterns = [
    url(r"^$", FriendList.as_view(), name="list"),
]
