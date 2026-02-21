"""
Week 04 - Abstraction
"""

from abc import ABC, abstractmethod

class Bank(ABC): 
    
    @abstractmethod
    def get_interest_rate(self):
        pass

class BankA(Bank):
    def get_interest_rate(self):
        return 5
    
class BankB(Bank):
    def get_interest_rate(self):
        return 10
    

bank1 = BankA()
bank2 = BankB()

print(bank1.get_interest_rate())
print(bank2.get_interest_rate())