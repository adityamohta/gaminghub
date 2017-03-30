"""hub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from chat.views import *


urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^accounts/", include("accounts.urls", namespace="accounts")),
    url(r"^friends/", include("friends.urls", namespace="friends")),
    url(r"^chat/$", RoomList.as_view(), name="room_list"),
    url(r"^chat/(?P<username>[\w.@+-]+)/$", RoomDetailView.as_view(), name="room_detail"),
    url(r"^chat/room/(?P<pk>\d+)/$", RoomMessageListAPIView.as_view(), name="room_message_list"),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
