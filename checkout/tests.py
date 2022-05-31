from django.test import TestCase


class CheckoutTestCases(TestCase):
    """ checkoout tests """

    def test_get_checkout_page(self):
        """ get checkout 200 """
        response = self.client.get('checkout/checkout.html')
        self.assertEqual(200, response.status)

    def test_get_checkout_complete_page(self):
        """ get checkout complete 200 """
        response = self.client.get('checkout/checkout_complete.html')
        self.assertEqual(200, response.status)
