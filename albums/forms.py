# -*- coding: utf-8 -*-

from django import forms

class AlbumForm(forms.Form):
    artist = forms.CharField(required=True, max_length=100, label="Artist")
    title = forms.CharField(required=True, max_length=100, label="Title")