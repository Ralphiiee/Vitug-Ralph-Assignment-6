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
            self.__rate = MortgageRate[str_rate_value]
        except Exception as e:
            raise ValueError("Rate provided is invalid.")
        
        #try and except block is initiated to catch an exception that will raise a value error that returns a string message
        try:
            self.__frequency = PaymentFrequency[str_frequency_value]
        except Exception as e:
            raise ValueError("Frequency provided is invalid.")
        
        #try and except block is initiated to catch an exception that will raise a value error that will return a string message
        try:
            self.__amortization = VALID_AMORTIZATION[str_amortization_value]
        except Exception as e:
            raise ValueError("Amortization provided is invalid.")
        
        #Defining an accessor that will return loan amount
        @property
        def loan_amount(self):
            return self.__loan_amount
        
        #Defining mutator that will raise a value error when amount is less than zero
        @loan_amount.setter
        def loan_amount(self, value):
            if value <= 0:
                raise ValueError("Loan amount must be positive ")
            self.__loan_amount = value


        pass