from django.conf.urls import patterns, include, url
from django.shortcuts import redirect
from sgtioapp import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'introproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^sgtioapp/$', views.sgtio_template),
)
