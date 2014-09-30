from django.conf.urls import patterns, include, url
from companies import views

urlpatterns = patterns('',
        url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
        url(r'^detail/$', views.detail_view, name='detail'),
        url(r'^$', views.index_view, name='index'),
        url(r'^analysis/$', views.analysis_view, name='comp_anal'),
        url(r'^analysis2/$', views.analysis2_view, name='comp_anal2'),
        url(r'^index2/$', views.index2_view, name='index2'),
        )
