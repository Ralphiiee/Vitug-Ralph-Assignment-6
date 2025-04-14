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
            Mortgage(-10000, 0.0519, "montly", 25)

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
        rate = 0.0599
        frequency = "monthly"
        amortization = 25
        expected = Mortgage(amount, rate, frequency, amortization)

        #Act and Assert
        self.assertEqual(expected.amount, 50000)
        self.assertEqual(expected.__rate, )
        self.assertEqual(expected.__frequency, "monthly")
        self.assertEqual(expected.__amortization, 25)



if __name__ == "__main__":
    unittest.main()


