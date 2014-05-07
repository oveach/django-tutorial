# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from models import Album
from forms import AlbumForm

# albums list
def index(request):
    # get albums from database
    albums = request.db_session.query(Album).order_by(Album.id)

    return render(request, "index.html", {
        'albums': albums,
    })

# create / update album
def album(request, album_id = None):
    if album_id is not None:
        album = request.db_session.query(Album).get(album_id)
    else:
        album = Album()

    if request.method == 'POST':
        if 'cancel' in request.POST:
            return redirect('index')
        form = AlbumForm(request.POST)
        if form.is_valid():
            album.title = form.cleaned_data['title']
            album.artist = form.cleaned_data['artist']
            request.db_session.add(album)
            request.db_session.commit()
            return redirect('index')
    elif album_id is not None:
        form = AlbumForm(album.__dict__)
    else:
        form = AlbumForm()

    return render(request, "album.html", {'form': form, 'album_id': album_id})

# delete album
def album_delete(request, album_id):
    if request.method == 'POST':
        if 'cancel' in request.POST:
            return redirect('index')
        else:
            request.db_session.query(Album).filter_by(id=album_id).delete()
            request.db_session.commit()
            return redirect('index')
    else:
        album = request.db_session.query(Album).get(album_id)

    return render(request, "album_delete.html", {'album': album})