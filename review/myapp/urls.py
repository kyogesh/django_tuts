from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^(?P<poll_id>\d+)/$',
                           views.detail, name='detail'),
                       url(r'^(?P<poll_id>\d+)/results/$',
                           views.results, name='results'),
                       url(r'^(?P<poll_id>\d+)/vote/$',
                           views.vote, name='vote'),
                       url(r'^register/$',
                           views.register, name='register'),
                       url(r'^signin/$',
                           views.signin, name='signin'),
                       url(r'^signoff/$',
                           views.signoff, name='signoff'),
                       url(r'^addpoll',
                           views.addpoll, name='addpoll'), )
