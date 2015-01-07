from django.conf.urls import patterns, include, url
from Startups.views import index_view
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Startups.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^$', index_view, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^companies/', include('companies.urls')),
    # url(r'^profiles/', include('profiles.urls')),
    url(r'^index/', include('profiles.urls')),
    # url(r'^hello/$', hello_view),
)
