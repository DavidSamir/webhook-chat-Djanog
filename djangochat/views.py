from django.contrib.auth import login
from django.shortcuts import render, redirect
from room.models import Room


def createRoom(request):
    if request.method == 'POST':
        if request.POST.get('name'):
            slg = request.POST.get('name').replace(' ', '')
        else:
            slg = request.POST.get('name')

        p = Room(
            name=request.POST.get('name'),
            slug=slg,
            description=request.POST.get('description'),
        )
        p.save()
        return redirect('rooms')
    else:
        return render(request, 'core/create-room.html')
