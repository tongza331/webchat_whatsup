# chat/routing.py
from django.conf.urls import url
from django.urls import re_path

from chat import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
    # re_path(r'ws/chat/(?P<room_name>\w+)/(?P<username>\w+)$', consumers.ChatConsumer.as_asgi()),
    # url(r'^ws/chat/(?P<room_name>[^/]+)(?P<username>[^/]+)/$', consumers.ChatConsumer.as_asgi()),
    # re_path(r'^ws/chat/(?P<room_name>[^/]+)(?P<username>[^/]+)/$', consumers.ChatConsumer.as_asgi()),
]