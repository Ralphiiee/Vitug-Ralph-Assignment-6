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
            self.__amortization = [VALID_AMORTIZATION][str_amortization_value]
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

        #Defining an accessor that will return rate
        @property
        def rate(self):
            
            return self.__rate
        
        #Defining mutator that contains try and except block. it will catch value error and return a string value
        @rate.setter
        def rate(self, rate_value):
            try:
                self.__rate = MortgageRate[rate_value]
            except Exception:
                raise ValueError("Rate provided is invalid.")
            
        #defining an accessor that will return frequency
        @property
        def frequency(self):

            return self.__frequency
        
        #Defining mutator that contains try and except block, it will catch a value error and return a string value
        @frequency.setter
        def frequency(self, frequency_value):
            try:
                self.__frequency = PaymentFrequency[frequency_value]
            except Exception:
                raise ValueError("Frequency provided is invalid.")
            
        #Defining an accessor that will return valid amortization
        @property
        def amortization(self):

            return self.__amortization
        
        #defining mutator that contains try and except block, it will catch a value error and return a string value
        @amortization.setter
        def amortization(self, amortization_value):
            try:
                self.__amortization = [VALID_AMORTIZATION][amortization_value]
            except Exception:
                raise ValueError("amortization provided is invalid.")


    #Defining a method that will calculate the payment for mortgage. formula is as per instructions
        def calculate_payment(self) -> float:

            """
            Args: calculate payment using given formula
            calculate_payment: returns a float value
            """

            pay_frequency = {
                "WEEKLY" : 52,
                "BI-WEEKLY" : 26,
                "MONTHLY" : 12
            }
            
            payment_per_year = pay_frequency.get(self.__frequency.lower())
            if not payment_per_year:
                raise ValueError ("Invalid payment frequency")
            
            principal = self.loan_amount
            annual_rate = self.rate.value
            periods = self.__amortization * payment_per_year
            periodic_rate = annual_rate / payment_per_year

            #Mortgage formula as provided
            numerator = periodic_rate * (1 +periodic_rate) ** periods
            denominator = (1 + periodic_rate) ** periods - 1
            payment = principal * (numerator / denominator)

            return round(payment, 2)
        

        pass

mortgage = Mortgage(123456.12, "FIXED_5", "MONTHLY", 10)
print(mortgage.calculate_payment())
