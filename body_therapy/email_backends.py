import requests
from django.core.mail.backends.base import BaseEmailBackend
from django.conf import settings


class BrevoAPIEmailBackend(BaseEmailBackend):
    """
    Custom email backend that sends emails via the Brevo
    transactional email HTTP API instead of SMTP.

    Render blocks outbound SMTP ports (25, 465, 587) on its
    free tier, so this backend uses HTTPS (port 443) instead.
    """

    API_URL = "https://api.brevo.com/v3/smtp/email"

    def send_messages(self, email_messages):
        if not email_messages:
            return 0

        sent_count = 0
        for message in email_messages:
            if self._send(message):
                sent_count += 1
        return sent_count

    def _send(self, message):
        api_key = settings.BREVO_API_KEY
        if not api_key:
            if not self.fail_silently:
                raise ValueError("BREVO_API_KEY is not set.")
            return False

        headers = {
            "accept": "application/json",
            "api-key": api_key,
            "content-type": "application/json",
        }

        payload = {
            "sender": {"email": message.from_email},
            "to": [{"email": addr} for addr in message.to],
            "subject": message.subject,
            "textContent": message.body,
        }

        try:
            response = requests.post(
                self.API_URL, json=payload, headers=headers, timeout=10
            )
            response.raise_for_status()
            return True
        except requests.RequestException:
            if not self.fail_silently:
                raise
            return False