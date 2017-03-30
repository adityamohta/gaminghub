from django.contrib import admin
from .models import *


class MessageInLine(admin.TabularInline):
    model = Message


class RoomModelAdmin(admin.ModelAdmin):

    inlines = [
        MessageInLine
    ]

    class Meta:
        model = Room

admin.site.register(Room, RoomModelAdmin)
