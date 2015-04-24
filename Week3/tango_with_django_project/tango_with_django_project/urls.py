from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings  # New Import
from django.conf.urls.static import static  # New Import
import rango.views

if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'tango_with_django_project_17.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^$', rango.views.main),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^rango/', include('rango.urls')),  # ADD THIS NEW TUPLE!
                       )

# UNDERNEATH your urlpatterns definition, add the following two lines:
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
         'serve',
         {'document_root': settings.MEDIA_ROOT}), )

