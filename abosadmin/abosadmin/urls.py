from django.conf.urls import patterns, include, url
from django.contrib import admin
import debug_toolbar


urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'abosadmin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^hoster/', include('hoster.urls', namespace='hoster')),
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^webblog/', include('webblog.urls', namespace='webblog')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^__debug__/', include(debug_toolbar.urls)),
    url(r'^admin/uwsgi/', include('django_uwsgi.urls')),
)
