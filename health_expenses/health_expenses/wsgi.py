"""
WSGI config for health_expenses project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'health_expenses.settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'health_expenses.health_expenses.settings')

application = get_wsgi_application()
