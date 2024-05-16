from django.urls import path
from .views import email_sender

urlpatterns = [
    path('send_email/', email_sender.as_view(), name="send-email"),
]
