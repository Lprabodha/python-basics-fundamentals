"""
Week 02 - Data Types (Epic Learn - Python Master Course)
"""

# int (Integer)
a = 10
b = -45
print("a:", a, "| type:", type(a))
print("b:", b, "| type:", type(b))

# float
x = 3.5
y = -5.5
print("x:", x, "| type:", type(x))
print("y:", y, "| type:", type(y))

# bool
is_active = True
is_blocked = False
print("is_active:", is_active, "| type:", type(is_active))
print("is_blocked:", is_blocked, "| type:", type(is_blocked))

# complex
c1 = 5 + 3j
c2 = complex(5, 3.5)
print("c1:", c1, "| type:", type(c1))
print("c2:", c2, "| type:", type(c2))
print("c2 real:", c2.real)
print("c2 imag:", c2.imag)

# string
s = "Epic Learn"
print("s:", s, "| type:", type(s))

# list
fruits = ["apple", "banana", "cherry"]
print("fruits:", fruits, "| type:", type(fruits))

# tuple (immutable)
colors = ("red", "green", "blue")
print("colors:", colors, "| type:", type(colors))

# set (unique values)
numbers = {1, 2, 2, 3, 3, 4}
print("numbers:", numbers, "| type:", type(numbers))

# dictionary (key-value)
user = {"name": "John", "age": 36}
print("user:", user, "| type:", type(user))
