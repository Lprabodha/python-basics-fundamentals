"""
Week 03 - Collections (Tuple, Dictionary, Set)
Epic Learn - Python Master Course
"""

# ---------------------------
# Tuple (Immutable)
# ---------------------------
colors = ("red", "green", "blue")
print("Tuple:", colors)
print("First:", colors[0])
print("Last:", colors[-1])
print("Slice 0:2:", colors[0:2])

# colors[0] = "black"  # ❌ Error (tuple is immutable)


# ---------------------------
# Dictionary (Key-Value)
# ---------------------------
student = {"name": "Kamal", "age": 20, "active": True}
print("\nDictionary:", student)
print("Student Name:", student["name"])
print("Student Age:", student["age"])

# Update values
student["name"] = "Nimal"
student["age"] = 25
print("Updated:", student)

# Remove key
student.pop("active")
print("After pop:", student)

# Nested dictionary + list
user = {
    "id": 1,
    "profile": {"name": "Nimal", "country": "LK"},
    "role": ["admin", "editor"]
}
print("\nNested Dictionary:", user)
print("Profile Name:", user["profile"]["name"])
print("First Role:", user["role"][0])


# ---------------------------
# Set (Unique values)
# ---------------------------
nums = {1, 2, 2, 3}
print("\nSet:", nums)  # duplicates removed automatically

nums.add(4)
print("After add:", nums)

nums.remove(2)
print("After remove:", nums)

# Real example: remove duplicate emails
emails = ["a@test.com", "b@test.com", "a@test.com"]
unique_emails = set(emails)
print("\nUnique emails:", unique_emails)
