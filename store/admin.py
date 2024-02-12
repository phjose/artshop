from django.contrib import admin

from .models import Artist, Painting, Support, Technique


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['user', 'inst_url']
    list_editable = ['inst_url']


@admin.register(Painting)
class PaintingAdmin(admin.ModelAdmin):
    list_display = ['name', 'pub_date', 'artist', 'price', 'available']
    list_filter = ['artist', 'available', 'price']
    list_editable = ['price', 'available']


admin.site.register(Support)
admin.site.register(Technique)
