"""
Week 03 - Conditional Statements (if / elif / else)
Epic Learn - Python Master Course
"""

marks = 30

if marks >= 75:
    print("Grade A")
elif marks >= 65:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

# Example: backend style validation
age = 20
if age >= 18:
    print("Allowed (Age Verified)")
else:
    print("Not Allowed")
