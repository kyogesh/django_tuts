from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'review.views.home', name='home'),
                       url(r'^myapp/',
                           include('myapp.urls', namespace='myapp')),
                       url(r'^forms/',
                           include('formtut.urls', namespace='forms')),
                       url(r'^admin/', include(admin.site.urls)), )

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
                            (r'media/(?P<path>.*)',
                             'serve',
                             {'document_root': settings.MEDIA_ROOT}), )
