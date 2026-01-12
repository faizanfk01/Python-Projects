# Map, Filter and Reduce:

# Map:

# map(): Applies a function to every item in an iterable and returns a map object (an iterator).
# It is used for transforming items without changing the number of elements.

def cube(x):
    return x * x * x

print(cube(2))

l = [1, 2, 3, 4, 5, 6, 7, 8]
newl = list(map(cube, l))

print(newl)


# Filter:

# filter(): Applies a function to each item and returns only those for which the function returns True.
# It is used for filtering items based on a condition.

def filter_function(a):
    return a > 4

newl2 = list(filter(filter_function, l))

print(newl2)


# Reduce:

# reduce(): Applies a rolling computation to sequential pairs of values in an iterable.
# It is used for performing cumulative operations like summing or multiplying elements.

from functools import reduce

numbers = [1, 2, 3, 4, 5]

def mysum(x, y):
    return x + y

sum = reduce(mysum, numbers)

print(sum)