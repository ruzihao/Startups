from django.conf.urls import patterns, include, url
from Startups.views import hello_view
import companies

from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Startups.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^companies/', include('companies.urls')),
    url(r'^profiles/', include('profiles.urls')),
    url(r'^hello/$', hello_view),
)
