# A set in Python is an unordered collection of unique elements. 
# It is mutable but does not allow duplicate values.

my_set = {1, 2, 3, 4, 2}       # Duplicate '2' is ignored
print(my_set)                 # Output: {1, 2, 3, 4}

my_set.add(5)                 # Adding an element
print(my_set)                 # Output: {1, 2, 3, 4, 5}