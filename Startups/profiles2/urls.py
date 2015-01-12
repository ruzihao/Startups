from django.conf.urls import patterns, include, url
from profiles2 import views

urlpatterns = patterns('',
        url(r'^(?P<cid>\d+)/$', views.profiles_view, name='profiles'),
        )
