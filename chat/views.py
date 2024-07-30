from django.shortcuts import render, redirect, get_object_or_404
from .models import Room

def create_room(request):
    if request.method == 'POST':
        room_name = request.POST.get('room_name')
        room, created = Room.objects.get_or_create(name=room_name)
        return redirect('room', room_name=room.name)
    return render(request, 'index.html')

def room(request, room_name):
    room = get_object_or_404(Room, name=room_name)
    return render(request, 'room.html', {
        'room': room
    })