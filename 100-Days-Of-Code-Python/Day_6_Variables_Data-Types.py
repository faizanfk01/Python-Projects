# Variables:

# Variables are used to store data values in Python.
# Each variable below has a different data type like int, float, str, bool, None, and complex.

a = 20
b = 20.5
c = "Faizan"
d = True
e = None
f = complex(3, 6)

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

print("**************************")

# Data Type:

# The type() function is used to check the data type of a variable.
# It helps us understand how Python is treating the stored value.

print("The type of a is ", type(a))
print("The type of b is ", type(b))
print("The type of c is ", type(c))
print("The type of d is ", type(d))
print("The type of e is ", type(e))
print("The type of f is ", type(f))

print("**************************")

# List, Tuple and Dictionary:

# A list is an ordered, mutable collection of items in Python.
# It can hold multiple data types like numbers and strings.

list1 = [1, 2, 3, 4, 5, "Pakistan", "India", "America", "Afghanistan", 'Iran']
print(list1)
print(type(list1))

print("**************************")

# A tuple is similar to a list, but it is immutable (cannot be changed).
# It is used to store a fixed collection of items.

tuple1 = (10, 9, 8, 7, 6, 5, "Apple", "Orange", "Pineapple", "Peach", "Graps")
print(tuple1)
print(type(tuple1))

print("**************************")

# A dictionary stores data in key-value pairs.
# It is mutable and allows fast lookup of values using keys.

dict1 = {"Name" : "Faizan", "Age" : 20, "Programmer" : True}
print(dict1)
print(type(dict1))
