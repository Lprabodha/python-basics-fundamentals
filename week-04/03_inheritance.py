"""
Week 04 - Inheritance
"""

# Single + Multi-level Inheritance

class Phone1:
    def feature1(self):
        print("Camera")
        
class Phone2(Phone1):
    def feature2(self):
        print("Internet")

class Phone3(Phone2):
    def feature3(self):
        print("Bluetooth")
        

phone = Phone3()

phone.feature1()
phone.feature2()
phone.feature3()