from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from friendlist.routing import websocket_urlpatterns  # Import your WebSocket URL patterns

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),  # Default ASGI application for HTTP requests
        "websocket": URLRouter(
            websocket_urlpatterns  # Your WebSocket URL patterns
        ),
    }
)
