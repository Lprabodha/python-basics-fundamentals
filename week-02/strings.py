"""
Week 02 - Strings (Epic Learn - Python Master Course)
"""

x = "Epic Learn"
print("x:", x)
print("type:", type(x))

# Indexing
# Epic Learn
# 0123456789
# -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

print("First character:", x[0])     # E
print("Negative index first:", x[-10])  # E

# Slicing (substring)
print("Substring (0:4):", x[0:4])   # Epic
print("Substring (5:10):", x[5:10]) # Learn
print("Substring (5:):", x[5:])     # Learn

# Concatenation
s1 = "Epic"
s2 = "Learn"
print("Concat:", s1 + s2)
print("Concat with space:", s1 + " " + s2)

# String + int (error) -> fix using str()
s3 = 55
# print(s1 + " " + s2 + s3)  # ❌ Error
print("Fixed:", s1 + " " + s2 + " " + str(s3))

# in / not in
name = "Epic Learn"
print("'E' in name:", "E" in name)
print("'z' in name:", "z" in name)
print("'E' not in name:", "E" not in name)

# String methods
name = "epic learn"
print("Original:", name)
print("upper:", name.upper())
print("lower:", name.lower())
print("title:", name.title())
print("capitalize:", name.capitalize())

# find vs index
print("find('i'):", name.find("i"))         # returns index or -1
print("find('learn'):", name.find("learn")) # 5

print("index('learn'):", name.index("learn"))  # returns index or error
# print(name.index("zzz"))  # ❌ ValueError

# center
print("center 20 '-':", name.center(20, "-"))
print("center 30 '*':", name.center(30, "*"))

# strip
name_space = "   epic learn   "
print("strip:", name_space.strip())
print("lstrip:", name_space.lstrip())
print("rstrip:", name_space.rstrip())

name2 = "###epic learn###"
print("strip default:", name2.strip())
print("strip '#':", name2.strip("#"))

# startswith / endswith
print("startswith('e'):", name.startswith("e"))
print("endswith('n'):", name.endswith("n"))

# replace
print("replace learn->school:", name.replace("learn", "school"))

# join (correct way)
words = ["Epic", "Learn", "Python"]
print("join with '-':", "-".join(words))

# split (correct way)
sentence = "epic learn python"
print("split by space:", sentence.split(" "))
