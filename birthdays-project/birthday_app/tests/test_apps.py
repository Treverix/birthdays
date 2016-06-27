from django.test import TestCase
from django.apps import apps


class BirthdayAppTestCase(TestCase):

    def test_that_app_is_properly_configured(self):
        # Given

        # When
        config = apps.get_app_config('birthday')

        # Then
        self.assertEqual('birthday', config.name)
        self.assertEqual('Birthday App', config.verbose_name)
