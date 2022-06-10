"""
Testing the methods
"""


import unittest
from unittest import TestCase
from palindrome import is_palindrome
from prime_number import is_prime


class TestingFunction(TestCase):
    """Class with the testing cases"""

    def test_is_palindrome(self):
        """Testing is_palindrome method"""
        self.assertEqual(is_palindrome('primo'), False)

        self.assertEqual(is_palindrome('Somos o no somos'), True)

        self.assertEqual(is_palindrome('This is a test'), False)
        
        self.assertEqual(is_palindrome('TAco cAt'), True)

    
    def test_is_prime(self):
        """Testing is_prime method"""
        self.assertEqual(is_prime(25), False)
        self.assertEqual(is_prime(87), False)
        self.assertEqual(is_prime(97), True)
        self.assertEqual(is_prime(73), True)
        self.assertEqual(is_prime(57), False)
        self.assertEqual(is_prime(34), False)
        self.assertEqual(is_prime(71), True)

    
if __name__ == '__main__':
    unittest.main()