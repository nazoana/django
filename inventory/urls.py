from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('inventory.views',
    url(r'^$', 'index', name='index'),
    url(r'^display_meta/$', 'display_meta'),
    url(r'^search/$', 'search', name='search'),
    url(r'^incoming/$', 'incoming', name='incoming'),
    url(r'^dispatching/$', 'dispatching', name='dispatching'),
    url(r'^returning/$', 'returning', name='returning'),
    url(r'^reports/$', 'reports', name='reports'),
    url(r'^help/$', 'help', name='help'),
    url(r'^contact/$', 'contact', name='contactus'),
    url(r'^faq/$', 'faq', name='faq'),
    #url(r'^(?P<blog_id>\d+)/$', 'detail'),
    #url(r'^(?P<blog_id>\d+)/results/$', 'results'),
    #url(r'^(?P<blog_id>\d+)/vote/$', 'vote'),
)
