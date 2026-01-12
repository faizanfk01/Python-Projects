# List methods in Python are built-in functions that allow you to manipulate list data easily,
# such as adding, removing, sorting, or reversing elements.

my_list = [3, 1, 4, 1, 5]

my_list.append(9)           # Adds 9 to the end → [3, 1, 4, 1, 5, 9]
my_list.insert(2, 7)        # Inserts 7 at index 2 → [3, 1, 7, 4, 1, 5, 9]
my_list.remove(1)           # Removes first occurrence of 1 → [3, 7, 4, 1, 5, 9]
my_list.pop()               # Removes last element (9) → [3, 7, 4, 1, 5]
my_list.sort()              # Sorts the list → [1, 3, 4, 5, 7]
my_list.reverse()           # Reverses the list → [7, 5, 4, 3, 1]
my_list.extend([10, 11])    # Adds multiple elements → [7, 5, 4, 3, 1, 10, 11]
copied = my_list.copy()     # Creates a shallow copy of the list
count_5 = my_list.count(5)  # Counts occurrences of 5 → 1
index_4 = my_list.index(4)  # Finds index of first 4 → 2
del my_list[1]              # Deletes element at index 1 → [7, 4, 3, 1, 10, 11]

# Additional operations
multiplied = my_list * 2          # Repeats list → [7, 4, 3, 1, 10, 11, 7, 4, 3, 1, 10, 11]
exists = 10 in my_list            # Checks for existence → True
squares = [x**2 for x in range(5)]  # List comprehension → [0, 1, 4, 9, 16]

# Outputs for reference
print("Final List:", my_list)
print("Copied List:", copied)
print("Count of 5:", count_5)
print("Index of 4:", index_4)
print("Multiplied:", multiplied)
print("Exists 10?:", exists)
print("Squares:", squares)