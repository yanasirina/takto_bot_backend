from unittest import TestCase

from lib.string import clean_phone_number


class String(TestCase):
    def test_clean_phone_number(self):
        phone_number = '+7 (123) 456-78-90'
        expected_phone_number = '+71234567890'
        actual_phone_number = clean_phone_number(phone_number)
        self.assertEqual(expected_phone_number, actual_phone_number)
