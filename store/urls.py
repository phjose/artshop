from django.urls import path
from store import views


app_name = 'store'
urlpatterns = [
    path('', views.index, name='index'),
    path('gallery/<int:page>/', views.gallery, name='gallery'),

    # Listado publico de artistas
    path('artists/', views.artists, name='artists'),

    # Detalle publico de artistas por pk.
    path('artists/<int:pk>/', views.artist, name='artist'),

    # Detalle publico de pinturas por pk
    path('painting/<int:pk>/', views.painting_detail, name='painting_detail'),

    path('process/', views.process, name='process'),
    path('future/', views.future, name='future'),
    path('news/', views.news, name='news'),
    path('searched/', views.search, name='search'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
