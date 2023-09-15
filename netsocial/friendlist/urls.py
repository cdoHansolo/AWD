from django.core.asgi import get_asgi_application
from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from . import consumers

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(
        # Define your WebSocket URL routing here
        path("ws/some_path/", consumers.ChatConsumer.as_asgi()),
    ),
})
