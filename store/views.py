from django import forms
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

from store.models import Painting, Artist
from store.forms import SignUpForm


def index(request):
    context = {}
    return render(request, 'store/index.html', context)


def gallery(request, page):
    inum = 20
    pagination = Painting.objects.all().count() > inum
    paintings_all = Painting.objects.all()  # order_by('-pub_date')
    p = Paginator(paintings_all, inum)  # show inum paintings per page.
    paintings_p = p.get_page(page)

    nums = "a" * paintings_p.paginator.num_pages
    context = {"paintings_all": paintings_all, "paintings_p": paintings_p, "nums": nums, "pagination": pagination, }
    return render(request, 'store/gallery.html', context)


def artists(request):
    artists = Artist.objects.order_by('user__username')
    context = {'artists': artists, 'session': request.session, }
    return render(request, 'store/artists.html', context)


def artist(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    paintings = Painting.objects.filter(artist=pk)
    context = {'artist': artist, 'paintings': paintings, }
    return render(request, 'store/artist.html', context)


def process(request):
    context = {}
    return render(request, 'store/process.html', context)


def future(request):
    context = {}
    return render(request, 'store/future.html', context)


def news(request):
    context = {}
    return render(request, 'store/news.html', context)


def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        if searched == '':
            context = {
                "searched": searched,
            }
        else:
            artist = Artist.objects.filter(user__username__contains=searched).order_by('user')
            paintings_name = Painting.objects.filter(name__contains=searched).order_by('-pub_date')
            paintings_category = Painting.objects.filter(category__contains=searched).order_by('-pub_date')
            paintings_artist = Painting.objects.filter(artist__user__username__contains=searched).order_by('-pub_date')
            paintings_technique = Painting.objects.filter(technique__name__contains=searched).order_by('-pub_date')
            paintings = paintings_name | paintings_category | paintings_artist | paintings_technique
            context = {
                "artist": artist,
                "paintings": paintings,
                "searched": searched,
            }

        return render(request, 'store/searched.html', context)

    else:
        inum = 30
        paintings_all = Painting.objects.order_by('-pub_date')
        p = Paginator(paintings_all, inum)  # show inum paintings per page.
        paintings_p = p.get_page(1)

        nums = "a" * paintings_p.paginator.num_pages
        context = {"paintings_all": paintings_all, "paintings_p": paintings_p, "nums": nums, }
        return render(request, 'store/gallery.html', context)


def painting_detail(request, pk):
    # cart = Cart(request)
    # cart_products = cart.get_products()

    painting = get_object_or_404(Painting, pk=pk)
    related_paintings = Painting.objects.filter(artist=painting.artist).exclude(pk=pk)

    context = {'painting': painting, 'related_paintings': related_paintings, }
    return render(request, 'store/painting_detail.html', context)


def login_user(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('store:gallery', page=1)
        else:
            return redirect('store:login')
    else:
        context = {}
        return render(request, 'store/index.html', context)


def logout_user(request):

    logout(request)
    return redirect('store:index')
