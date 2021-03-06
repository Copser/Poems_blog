"""
WSGI config for poets_blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "poets_blog.settings")

application = Cling(get_wsgi_application())
