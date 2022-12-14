"""
ASGI config for DiziAttendance project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""


from django.core.asgi import get_asgi_application
import os
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator




os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DiziAttendance.settings')

application = get_asgi_application()

import Attendance.routing

application = ProtocolTypeRouter(
    {
        "http": application,
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(Attendance.routing.websocket_urlpatterns))
        ),
    }
)