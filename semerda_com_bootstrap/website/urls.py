# Defaults
from django.conf.urls.defaults      		import patterns, include, url

# Main website
from semerda_com_bootstrap.website.views    import home_view, about_view


urlpatterns = patterns('',
    (r'^$', home_view),
    (r'^about/$', about_view),
)