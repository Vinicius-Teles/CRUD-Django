from django.conf.urls import patterns, url

from sales import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^sales/$', views.sales, name='sales'),
    url(r'^save/$', views.save, name='save'),
    url(r'^(?P<sale_id>\d+)/edit/$', views.edit, name='edit'),
    url(r'^search/$', views.search, name='search'),
    url(r'^(?P<sale_id>\d+)/delete/$', views.delete, name='delete'),
)