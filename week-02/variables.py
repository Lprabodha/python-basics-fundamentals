"""
Week 02 - Variables (Epic Learn - Python Master Course)

Program = Data + Instructions
Variable = a reference (name) that points to data in memory
"""

# Program = Data + Instructions
name = "Epic Learn"
age = 20

print("Name:", name)
print("Age:", age)

# Variable naming examples
my_name = "Lahiru"     # ✅ snake_case (recommended)
_my_age = 25           # ✅ can start with underscore
name2 = "Epic"         # ✅ numbers allowed (not first char)

# Case sensitive
value = 100
Value = 200
print("value:", value)
print("Value:", Value)

# Invalid variable names (DO NOT UNCOMMENT)
# 2name = "wrong"      # ❌ cannot start with a number
# my-name = "wrong"    # ❌ hyphen not allowed
# class = "wrong"      # ❌ keyword cannot be used

# Best practice: snake_case for Python
student_name = "Nimal"
student_age = 18

print("Student:", student_name, "| Age:", student_age)
