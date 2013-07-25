from django.conf.urls import patterns, include, url

from django.views.generic import ListView, DetailView

from greg1App.models import Person
from greg1App.views import PersonUpdateView


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'greg1Project.views.home', name='home'),
    # url(r'^greg1Project/', include('greg1Project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # greg1App urls
    url(r'^$', 'greg1App.views.home'),
    url(r'^person_list$', ListView.as_view(model=Person)),
    url(r'^person_detail/(?P<pk>\d+)$', DetailView.as_view(model=Person)),
    url(r'^person_update/(?P<pk>\d+)$', PersonUpdateView.as_view(success_url='/person_list')),
    url(r'^person_delete/(?P<pk>\d+)$', DetailView.as_view(model=Person)),
)
