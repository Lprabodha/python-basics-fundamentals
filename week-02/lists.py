"""
Week 02 - Lists (Epic Learn - Python Master Course)

List = ordered, mutable, allows duplicates
"""

# Create lists
list1 = []
list2 = list()

print("type(list1):", type(list1))
print("type(list2):", type(list2))

mylist = ["apple", "banana", "cherry"]
print("mylist:", mylist)

# Mixed data list (Python supports mixed types)
mylist3 = ["Nimal", 20, "Galle", 5, 3.5, False]
print("mylist3:", mylist3)

# Access elements using indexing
print("First element:", mylist3[0])
print("Last element:", mylist3[-1])

# Slicing
print("All elements:", mylist3[:])
print("First 3 elements:", mylist3[0:3])

# List is mutable (can change values)
mylist = ["apple", "banana", "cherry"]
mylist[1] = "orange"
print("After change:", mylist)

# List methods
# append()
mylist = ["apple", "banana", "cherry"]
mylist.append("orange")
print("append:", mylist)

# extend()
mylist = ["apple", "banana", "cherry"]
mylist2 = ["orange", "kiwi"]
mylist.extend(mylist2)
print("extend:", mylist)

# insert()
mylist = ["apple", "banana", "cherry"]
mylist.insert(1, "orange")
print("insert:", mylist)

# Bonus: remove / pop
mylist = ["apple", "banana", "cherry", "banana"]
mylist.remove("banana")  # removes first matching item
print("remove first banana:", mylist)

last_item = mylist.pop()  # removes last item
print("popped item:", last_item)
print("after pop:", mylist)
