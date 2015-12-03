from django.conf.urls import patterns, include, url

from django.contrib import admin
from Startups.views import home_view
from profiles.views import company_list
from profiles.views import search
from profiles.views import dataImport
from profiles.views import predict

urlpatterns = patterns('',
    url(r'^$', home_view, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^dataimport/(?P<param>.+)$', dataImport, name='dataImport'),
    url(r'^profiles/', include('profiles.urls')),
	url(r'^company/$', company_list, name='company_list'),
	url(r'^search/(?P<search_string>.+)$', search, name='search'),
	url(r'^predict/(?P<cid>\d+)/*$', predict, name='predict'),
	
	#url(r'^companies/', include('companies.urls')),
    # url(r'^hello/$', hello_view),
)
