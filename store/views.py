from django import forms
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User

from store.models import Painting, Artist
from store.forms import SignUpForm, UpdateArtistForm, PaintingForm


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


def artist_paintings(request, pk):
    artist_paintings = Painting.objects.filter(artist=pk)
    context = {'artist_paintings': artist_paintings, 'artist_pk': pk}
    return render(request, 'store/artist_paintings.html', context)


def add_painting(request):
    submitted = False
    artist = request.user.artist

    if request.method == 'POST':

        painting_form = PaintingForm(request.POST, request.FILES)
        if painting_form.is_valid():
            painting = painting_form.save(commit=False)
            painting.artist = artist
            painting.save()
            artist_paintings = Painting.objects.filter(artist=artist.pk)
            context = {'artist_paintings': artist_paintings, 'artist_pk': artist.pk, }
            return render(request, 'store/artist_paintings.html', context)
            # return HttpResponseRedirect('/artist_paintings/' + str(artist.pk) + '/')
    else:
        painting_form = PaintingForm
        #if 'submitted' in request.GET:
         #   submitted = True

        #context = {'painting_form': painting_form, 'submitted': submitted}
        context = {'painting_form': painting_form, }
        return render(request, 'store/add_painting.html', context)


def update_painting(request, pk):
    painting = Painting.objects.get(pk=pk)
    artist = request.user.artist
    painting_form = PaintingForm(request.POST or None, request.FILES or None, instance=painting)

    if painting_form.is_valid():
        painting = painting_form.save(commit=False)
        painting.artist = artist
        painting.save()
        return redirect('store:artist_paintings', pk=artist.pk)
    context = {'painting': painting, 'painting_form': painting_form, }
    return render(request, 'store/update_painting.html', context)


def delete_painting(request, pk):
    artist = request.user.artist
    painting = Painting.objects.get(pk=pk)
    if request.user.is_authenticated and artist.pk == painting.artist.pk:
        painting.delete()
        return redirect('store:artist_paintings', pk=artist.pk)

    return redirect('store:update_painting', pk=pk)


def update_artist(request, pk):

    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        current_artist = Artist.objects.get(pk=pk)
        artist_form = UpdateArtistForm(request.POST or None, request.FILES or None, instance=current_artist)

        if artist_form.is_valid():
            artist_form.save()
            login(request, current_user)
            return redirect('store:artist_detail', pk=pk)
        context = {'artist_form': artist_form, 'current_artist': current_artist, }
        return render(request, 'store/update_artist.html', context)
    else:
        return redirect('store:index')


def artists(request):
    artists = Artist.objects.order_by('user__username')
    context = {'artists': artists, 'session': request.session, }
    return render(request, 'store/artists.html', context)


def artist_detail(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    paintings = Painting.objects.filter(artist=pk)
    context = {'artist': artist, 'paintings': paintings, }
    return render(request, 'store/artist_detail.html', context)


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
            return redirect('store:index')
        else:
            return redirect('store:login')
    else:
        context = {}
        return render(request, 'store/index.html', context)


def logout_user(request):

    logout(request)
    return redirect('store:index')
