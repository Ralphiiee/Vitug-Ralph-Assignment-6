"""
Description: Enumerations to keep track of valid mortgage rates 
and payment frequencies. A list to keep track of valid amortization periods.
Author: ACE Department
Edited By: {Student Name}
Date: {Date}
Usage: The enumerations and list in this file may be used when working 
with mortgages to ensure only valid rates, frequencies and amortization 
periods are used.
"""


from enum import Enum

class MortgageRate(Enum): #initialing a class to contain the interest rate method
    """ MortgageRate consists of valid interest rate that corresponds the 
    type of mortgage

    FIXED rate is lower because it will not be affected by the market
    within the agreed upon duration of the contract.

    VARIABLE rate is higher because it follows the market's volatility,
    if the entire market is doing good, then the interest drops 

    """
    FIXED_5 = 0.0519
    FIXED_3 = 0.0589
    FIXED_1 = 0.0599
    VARIABLE_5 = 0.0649
    VARIABLE_3 = 0.0669
    VARIABLE_1 = 0.679

class PaymentFrequency(Enum): #initializing a class to contain the method for payment frequency
    """ PaymentFrequent class represents the frequency of payment.
    MONTHLY will assign payment for each month of the year
    BI_WEEKLY will assign payment twice, each month to a total of 26 payments per year
    WEEKLY will assign payment every week to a total of 52 payments per year
    """
    MONTHLY = 12
    BI_WEEKLY = 26
    WEEKLY = 52
    
VALID_AMORTIZATION = {5, 10, 15, 20, 25, 30}

