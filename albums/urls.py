from django.conf.urls import patterns, include, url

from albums import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'projet_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^album/(\d)?$', views.album, name='album'),
    url(r'^album/delete/(\d)+$', views.album_delete, name='album_delete'),
)
