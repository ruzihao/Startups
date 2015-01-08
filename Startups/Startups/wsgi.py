"""
WSGI config for Startups project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os, sys
if '/var/www/wandig.com/Startups/Startups' not in sys.path:
    sys.path.append('/var/www/wandig.com/Startups/Startups')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Startups.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
