"""
Week 03 - For Loop
Epic Learn - Python Master Course
"""

# Loop through a tuple
nums = (1, 2, 3, 4, 5)
for n in nums:
    print("Number:", n)

# Loop through dictionary
x = {
    "name": "Kamal",
    "age": 20,
    "gender": "male"
}

print("\nKeys:")
for key in x.keys():
    print(key)

print("\nValues:")
for value in x.values():
    print(value)

print("\nItems (key, value):")
for key, value in x.items():
    print(key, "=>", value)
