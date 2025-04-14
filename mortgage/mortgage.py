"""
Description: A class meant to manage Mortgage options.
Author: {Student Name}
Date: {Date}
Usage: Create an instance of the Mortgage class to manage mortgage records and 
calculate payments.
"""


from mortgage.pixell_lookup import MortgageRate, PaymentFrequency, VALID_AMORTIZATION

class Mortgage:
    """ Mortgage encapsulates the methods such as, MortgageRate which entails interest rate of chosen mortgage
    PaymentFrequency in which the frequency of payment per yer and lastly, VALID_AMORTIZATION is a list of durations
    """
    def __init__(self, loan_amount: float, rate: str, frequency: str, amortization: int):
        """
        Loan_Amount: returns an expected amount value in float form
        Rate: returns the interest rate value that will be in a string form
        Frequency: returns the frequency of payment in a string form
        Amortization: returns the duration of chosen loan in an integer form
        """

        #try and except block is initiated to catch an exception in which will raise a value error that returns a string value
        try:
            self.__rate = MortgageRate[rate.str]
        except Exception as e:
            raise ValueError("Rate provided is invalid.")
        
        #try and except block is initiated to catch an exception that will raise a value error that returns a string message
        try:
            self.__frequency = PaymentFrequency[frequency.str]
        except Exception as e:
            raise ValueError("Frequency provided is invalid.")
        
        #try and except block is initiated to catch an exception that will raise a value error that will return a string message
        try:
            self.__amortization = VALID_AMORTIZATION[amortization.int]
        except Exception as e:
            raise ValueError("Amortization provided is invalid.")
        
        pass