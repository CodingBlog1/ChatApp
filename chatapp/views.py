from django.shortcuts import render
from .models import Room,Message
from django.http import HttpResponse
from django.views import View

class AllRooms(View):
    def get(self,request):
        allroms = Room.objects.all()
        return render(request,"rooms.html",{"rooms":allroms})
        
            
class GetRoomBySlug(View):
    def get(self,request,slug):
        room_name=""
        room_name=Room.objects.filter(slug=slug)
        if room_name.exists():
            room_name=room_name.first().name
        messages=Message.objects.filter(room__slug__iexact=slug)

        return render(request, "room.html",{"room_name":room_name,"slug":slug,'messages':messages})
            