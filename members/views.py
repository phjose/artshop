from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from store.models import Painting, Artist

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            artist = Artist.objects.get(pk=user.artist.pk)
            paintings = Painting.objects.filter(artist=user.artist.pk)
            context = {'artist': artist, 'paintings': paintings }
            return render(request, 'store/artist_detail.html', context)
        else:
            messages.success(request, 'There was an error log in, try again')
            return redirect('login')
    else:
        context = {}
        return render(request, 'authenticate/login.html', context)
                