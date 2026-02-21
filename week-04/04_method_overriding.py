"""
Week 04 - Method Overriding
"""

class Animal:
    def sound(self):
        print("Animal makes sound")
    
class Cat(Animal):
    def sound(self):
        print("Meow")
        
class Dog(Animal):
    def sound(self):
        print("Woof")

cat = Cat()
dog = Dog()

cat.sound()
dog.sound()