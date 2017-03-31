from django.conf.urls import url, include
from chat.views import *


urlpatterns = [
    url(r"^rooms/$", RoomList.as_view(), name="room_list"),
    url(r"^api/rooms/$", RoomListApiView.as_view(), name="room_list_api"),
    url(r"^room/(?P<pk>\d+)/$", RoomMessageListAPIView.as_view(), name="room_message_list"),
    url(r"^room/(?P<username>[\w.@+-]+)/$", RoomDetailView.as_view(), name="room_detail"),
    # url(r"^chat/$", RoomList.as_view(), name="room_list"),
    # url(r"^chat/(?P<username>[\w.@+-]+)/$", RoomDetailView.as_view(), name="room_detail"),
    # url(r"^chat/room/(?P<pk>\d+)/$", RoomMessageListAPIView.as_view(), name="room_message_list"),
]
