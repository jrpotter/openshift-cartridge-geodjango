from django.test import TestCase

class BaseViewsTestCase(TestCase):
    """
    This is a basic, provided test to ensure one can access the homepage.
    """
    def test_index(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
