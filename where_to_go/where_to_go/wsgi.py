"""
WSGI config for blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application
# import where_to_go.where_to_go.settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'where_to_go.settings')

application = get_wsgi_application()
