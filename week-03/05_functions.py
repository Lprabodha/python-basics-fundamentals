"""
Week 03 - Functions
Epic Learn - Python Master Course
"""

def say_hello():
    print("Hello")

def show_sum(num1, num2):
    print("Sum:", num1 + num2)

def add(a, b):
    return a + b

def rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    print("Area:", area)
    print("Perimeter:", perimeter)


# Run examples
say_hello()
show_sum(5, 10)

result = add(10, 20)
print("Return add:", result)

rectangle(5, 3)
