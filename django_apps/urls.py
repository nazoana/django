from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_apps.views.home', name='home'),
    # url(r'^django_apps/', include('django_apps.foo.urls')),

	url(r'^inventory/', include('inventory.urls')),
	url(r'^bookstore/', include('bookstore.urls')),
	
    # Uncomment the admin/doc line below to enable admin documentation:
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
     # Static files (FOR DEVELOPMENT ONLY!)
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT}),
)

#if settings.DEBUG:
#	urlpatterns += patterns('django.contrib.staticfiles.views', url(r'^static/(?P<path>.*)$', 'serve'),)
