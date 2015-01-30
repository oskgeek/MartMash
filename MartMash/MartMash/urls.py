from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', \
        {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
    url(r'^$', include('frontend.urls')),
    url(r'^2015/', include('frontend.urls'))
)
