# Core Python modules
import os # Miscellaneous operating system interfaces

# Defaults
from django.conf.urls.defaults      import patterns, include, url

# Access settings
from django.conf                    import settings

# Can redirect directly to template bypassing a view
from django.views.generic.simple    import direct_to_template

# Uncomment the next two lines to enable the admin:
#from django.contrib                 import admin
#admin.autodiscover()

# Handling exceptions
# Ref: https://docs.djangoproject.com/en/dev/topics/http/views/
handler404 = 'semerda_com_bootstrap.views.exception_404_view'
handler500 = 'semerda_com_bootstrap.views.exception_error_view'
handler403 = 'semerda_com_bootstrap.views.exception_permission_denied_view'


urlpatterns = patterns('',
    # Include Website URLs
    (r'^', include('semerda_com_bootstrap.website.urls')),
    
    # Enables Django Admin URL
    #url(r'^admin/', include(admin.site.urls)),

    # Required for admin/media files access
    #url(r'^media/(.*)$', 'django.views.static.serve', { 
    #    'document_root': '/usr/share/pyshared/django/contrib/admin/media/',  # Path to Django install
    #    'show_indexes' : True, 
    #}), 
    
    # Serve static files
    # ref: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#module-django.contrib.staticfiles
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT,
         'show_indexes': True}),
)