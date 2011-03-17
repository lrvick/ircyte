from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'logger.views.index', name="index"),
    url(r'^chan/(?P<channel>[-\w]+)/$', 'logger.views.logview', name='log-view'),
    url(r'^nick/(?P<nick>.*)', 'logger.views.userview', name="user-view"),
    #url(r'^s/$', statsView, name='stats-view'),
    #url(r'^liveupdate/(?P<id>\d+)/$', liveupdate, name='liveupdate'), 
    url(r'^admin/', include(admin.site.urls)),
)
