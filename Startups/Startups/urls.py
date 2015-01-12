from django.conf.urls import patterns, include, url

from django.contrib import admin
from Startups.views import home_view
import profiles2
import profiles

urlpatterns = patterns('',
    url(r'^$', home_view, name='home'),
    url(r'^admin/', include(admin.site.urls)),
	
	url(r'^profiles/', include('profiles.urls')),
	url(r'company/$', profiles.views.company_list, name='company_list'),
	
	#backup pages
    url(r'^profiles2/', include('profiles2.urls')),
	url(r'company2/$', profiles2.views.company_list, name='company_list2'),
	
	#url(r'^companies/', include('companies.urls')),
    # url(r'^hello/$', hello_view),
)
