from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('bookstore.views',
    url(r'^$', 'index'),
    url(r'^display_meta/$', 'display_meta'),
    #url(r'^search-form/$', 'search_form'),
    url(r'^contact/$', 'contact', name='contact'),
    url(r'^search/$', 'search'),
)
