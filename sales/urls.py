from django.conf.urls import patterns, url

from sales import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
    url(r'^/save/$', views.save, name='save'),
    url(r'^(?P<product_id>\d+)/edit/$', views.edit, name='edit'),
    url(r'^(?P<product_id>\d+)/delete/$', views.delete, name='delete'),
)