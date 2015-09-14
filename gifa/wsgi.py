"""
WSGI config for gifa project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys

PROJECT_PATH = '/var/www/site/gifa'
PROJECT_PATH_MAIN = '/var/www/site/gifa/gifa/settings'

sys.path.insert(0, PROJECT_PATH)
sys.path.append(PROJECT_PATH_MAIN)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gifa.settings.staging")

application = get_wsgi_application()
