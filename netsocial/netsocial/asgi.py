"""
ASGI config for netsocial project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from friendlist import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'netsocial.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(
            routing.websocket_urlpatterns
    ),
})
