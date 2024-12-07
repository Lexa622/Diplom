from django.urls import path
from . views import *

urlpatterns = [
    path('chat/<str:recipient_username>/', chat_view, name='chat'),
]
