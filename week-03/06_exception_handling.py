"""
Week 03 - Exception Handling (try / except / finally)
Epic Learn - Python Master Course
"""

try:
    a = int(input("Enter First number: "))
    b = int(input("Enter Second number: "))

    print("Result:", a / b)

except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)

except ValueError:
    print("ValueError: Please enter valid numbers.")

except TypeError:
    print("TypeError: Invalid type operation.")

except Exception as e:
    print("Unknown Error:", e)

finally:
    print("Cleanup Done (finally always runs)")

print("Exit")
