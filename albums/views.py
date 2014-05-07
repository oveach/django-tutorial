# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from models import Session, Album
from forms import AlbumForm

# albums list
def index(request):
    # get albums from database
    session = Session()
    albums = session.query(Album).order_by(Album.id)

    return render(request, "index.html", {
        'albums': albums,
    })

# create / update album
def album(request, album_id = None):
    session = Session()
    
    if album_id is not None:
        album = session.query(Album).get(album_id)
    else:
        album = Album()

    if request.method == 'POST':
        if 'cancel' in request.POST:
            return redirect('index')
        form = AlbumForm(request.POST)
        if form.is_valid():
            album.title = form.cleaned_data['title']
            album.artist = form.cleaned_data['artist']
            session.add(album)
            session.commit()
            return redirect('index')
    elif album_id is not None:
        form = AlbumForm(album.__dict__)
    else:
        form = AlbumForm()

    return render(request, "album.html", {'form': form, 'album_id': album_id})

# delete album
def album_delete(request, album_id):
    session = Session()

    if request.method == 'POST':
        if 'cancel' in request.POST:
            return redirect('index')
        else:
            session.query(Album).filter_by(id=album_id).delete()
            session.commit()
            return redirect('index')
    else:
        album = session.query(Album).get(album_id)

    return render(request, "album_delete.html", {'album': album})