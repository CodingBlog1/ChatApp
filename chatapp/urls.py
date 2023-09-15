from django.urls import path
from .views import *


urlpatterns = [
    path("", AllRooms.as_view(), name="rooms"),
    path("<str:slug>", GetRoomBySlug.as_view(), name="room"),
]
