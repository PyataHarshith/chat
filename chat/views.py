from django.shortcuts import render, redirect
from .models import room, message
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def Room(request,Room):
    username = request.GET.get('username')
    room_details = room.objects.get(name = Room)
    return render(request,'room.html',{
        'username' : username,
        'room': Room,
        'room_details': room_details
    })

def checkview(request):
    Room_name = request.POST['room_name']
    username = request.POST['username']

    if room.objects.filter(name=Room_name).exists():
        return redirect('/'+Room_name+'?username='+username)
    else:
        new_room = room.objects.create(name = Room_name)
        new_room.save()
        return redirect('/'+Room_name+'?username='+username)

def send(request):
    Message = request.POST['message']
    Username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = message.objects.create(value = Message, user = Username, room = room_id)
    new_message.save()

    return HttpResponse('message sent successfully')

def getMessages(request,Room):
    room_details = room.objects.get(name = Room)

    messages = message.objects.filter(room = room_details.id)
    return JsonResponse({"messages":list(messages.values()) })