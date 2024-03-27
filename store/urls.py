from django.urls import path
from store import views


app_name = 'store'
urlpatterns = [
    path('', views.index, name='index'),

    path('gallery/<int:page>/', views.gallery, name='gallery'),
    # Detalle publico de pinturas por pk
    path('painting/<int:pk>/', views.painting_detail, name='painting_detail'),
    # Artist painting list
    path('artist_paintings/<int:pk>/', views.artist_paintings, name='artist_paintings'),
    # Add, update, delete paintings from an Artist logged.
    path('add_painting/', views.add_painting, name='add_painting'),
    path('update_painting/<int:pk>/', views.update_painting, name='update_painting'),

    # Listado publico de artistas
    path('artists/', views.artists, name='artists'),
    # Detalle publico de artistas por pk.
    path('artists/<int:pk>/', views.artist_detail, name='artist_detail'),
    # Update profile artist.
    path('update_artist/<int:pk>/', views.update_artist, name='update_artist'),

    path('process/', views.process, name='process'),
    path('future/', views.future, name='future'),
    path('news/', views.news, name='news'),
    path('searched/', views.search, name='search'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
