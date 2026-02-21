"""
Week 04 - Method Overloading (Python Style)
"""

class Calculator:
    
    def add(self, a=None, b=None, c=None):
        total = 0
        
        if a is not None and b is not None and c is not None:
            total = a + b + c
        elif a is not None and b is not None:
            total = a + b
        elif a is not None:
            total = a
        else:
            total = 0
            
        print(total)


calc = Calculator()

calc.add(2, 5, 10)
calc.add(2, 5)
calc.add(2)
calc.add()