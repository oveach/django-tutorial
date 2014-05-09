# -*- coding: utf-8 -*-

from django import forms

class AlbumForm(forms.Form):
    artist = forms.CharField(required=True, max_length=100, label="Artist", widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': "Artist"
    }))
    title = forms.CharField(required=True, max_length=100, label="Title", widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': "Title"
    }))