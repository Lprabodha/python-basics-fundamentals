"""
Week 03 - While Loop (break / continue)
Epic Learn - Python Master Course
"""

# ✅ Basic while
i = 1
while i <= 3:
    print("i:", i)
    i += 1

# ✅ break example
print("\nBreak example:")
i = 1
while True:
    print(i)
    if i == 3:
        break
    i += 1

# ✅ continue example
print("\nContinue example:")
j = 0
while j < 5:
    j += 1
    if j == 3:
        continue
    print(j)

# ⚠️ Infinite loop example (keep commented)
# while True:
#     print("Hello")
