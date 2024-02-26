from django.urls import path
from . import views

app_name = 'store'
urlpatterns = [
    path('', views.index, name='index'),
    path('gallery/<int:page>/', views.gallery, name='gallery'),
    path('artist/', views.artist, name='artist'),
    path('artist/<int:pk>/', views.artist_detail, name='artist_detail'),
    path('painting/<int:pk>/', views.painting_detail, name='painting_detail'),
    path('process/', views.process, name='process'),
    path('future/', views.future, name='future'),
    path('news/', views.news, name='news'),
    path('searched/', views.search, name='search'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
]
