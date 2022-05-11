""" doc string """
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """ doc string """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        """ doc string """
        import checkout.signals
