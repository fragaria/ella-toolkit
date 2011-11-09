import django.dispatch

publishable_email_sent = django.dispatch.Signal(providing_args=["subject", "message", "recipients"])
