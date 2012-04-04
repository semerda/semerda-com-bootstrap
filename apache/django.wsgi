import os
import sys

path = '/var/www/semerda_com_bootstrap/'
if path not in sys.path:
    sys.path.insert(0, '/var/www/semerda_com_bootstrap/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'semerda_com_bootstrap.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
