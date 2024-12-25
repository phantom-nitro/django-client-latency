"""
ASGI config for ping_site project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from decouple import config

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ping_site.settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', config('DJANGO_SETTINGS_MODULE', default='ping_site.settings.prod'))

application = get_asgi_application()
