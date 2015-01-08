from django.conf.urls import patterns, include, url
from profiles import views

urlpatterns = patterns('',
        # url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
        url(r'^(?P<cid>\d+)/$', views.profiles_view, name='profiles'),
        # url(r'^test/$', views.test_view, name='test'),
        # url(r'^company/$', views.analysis_view, name='comp_anal'),
        # url(r'^analysis2/$', views.analysis2_view, name='comp_anal2'),
        # url(r'^index2/$', views.index2_view, name='index2'),
        )
