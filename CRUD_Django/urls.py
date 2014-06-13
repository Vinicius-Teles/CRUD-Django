from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CRUD_Django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^sales/', include('sales.urls', namespace="sales")),
    url(r'^admin/', include(admin.site.urls)),
)
