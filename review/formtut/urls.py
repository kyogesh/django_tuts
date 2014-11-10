from django.conf.urls import url, patterns, include

from . import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^(?P<person_id>\d+)/$', views.detail, name='detail'),
                       url(r'^edit/(?P<person_id>\d+)/$', views.edit, name='edit'),
                       url(r'^save/(?P<person_id>\d+)/$', views.save, name='save'),
)
