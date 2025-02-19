"""
WSGI config for lindas_blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv  # Optional: for loading environment variables from a .env file

# Load environment variables from .env file if present
load_dotenv()

# Set the default settings module for the 'DJANGO_SETTINGS_MODULE' environment variable.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lindas_blog.settings')

# Get the WSGI application for the project.
application = get_wsgi_application()
