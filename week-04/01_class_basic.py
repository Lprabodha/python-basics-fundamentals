"""
Week 04 - Basic Class Example
"""

class Phone: 
    
    def __init__(self, name, model, color, height):
        self.name = name
        self.model = model 
        self.color = color 
        self.height = height 
    
    def call(self, number):
        print(f"{self.name} is calling {number}")
        
    def message(self, number, text):
        print(f"Sending message to {number}: {text}")


phone1 = Phone("Samsung", "S24", "Black", "6.1")

phone1.call("0777898458")
phone1.message("0771234567", "Hello!")