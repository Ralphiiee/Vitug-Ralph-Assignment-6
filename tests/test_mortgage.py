"""
Description: A class used to test the Mortgage class.
Author: {Student Name}
Date: {Date}
Usage: Use the tests encapsulated within this class to test the MortgagePayment class.
"""

from unittest import TestCase
from mortgage.mortgage import Mortgage
from mortgage.pixell_lookup import MortgageRate, PaymentFrequency
from unittest.mock import patch

class MortgageTests(TestCase):

    #unit test that will raise value error if amount is invalid
    def test_invalid_amount(self):
        with self.assertRaises(ValueError):
            Mortgage(-10000, 0.0519, "monthly", 25)

    #unit test that will raise value error if interest is invalid
    def test_invalid_interest_rate(self):
        with self.assertRaises(ValueError):
            Mortgage(100000, -2.0, "weekly", 15)

    #unit test that will raise value error if frequency is invalid
    def test_invalid_payment_frequency(self):
        with self.assertRaises(ValueError):
            Mortgage(50000, 0.0519, "daily", 25)

    #unit test that will raise value error if amortization is invalid
    def test_invalid_amortization(self):
        with self.assertRaises(ValueError):
            Mortgage(100000, 0.0519, "monthly", 1)

    #unit test to check valid input
    def test_valid_input(self):
        #Arrange
        amount = 500000
        rate = "FIXED_5"
        frequency = "monthly"
        amortization = 25
        expected = Mortgage(amount, rate, frequency, amortization)

        #Act and Assert
        self.assertEqual(expected.amount, 50000)
        self.assertEqual(expected.__rate, "FIXED_5")
        self.assertEqual(expected.__frequency, "monthly")
        self.assertEqual(expected.__amortization, 25)

    #unit test that checks negative amount then will raise value error if amount is negative
    def test_set_negative_amount(self):
        mortgage = Mortgage(500000, "FIXED_5", "monthly", 25)
        with self.assertRaises(ValueError):
            mortgage.loan_amount = -5000

    #unit test that check if amount is > zero, if not, it will raise a value error
    def test_set_zero_amount(self):
        mortgage = Mortgage(500000, "FIXED_5", "monthly", 25)
        with self.assertRaises(ValueError):
            mortgage.loan_amount = 0

    #unit test that returns a positive value
    def test_valid_amount(self):
        mortgage = Mortgage(500000, "FIXED_5", "monthly", 25)
        mortgage.loan_amount = 450000
        self.assertEqual(mortgage.loan_amount, 450000)


if __name__ == "__main__":
    unittest.main()


