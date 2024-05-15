from django.urls import path
from .views import email_sender

urlpatterns = [
    path('send_email/', email_sender, name="send-email"),
]
