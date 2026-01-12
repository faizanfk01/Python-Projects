# Set Methods in Python

a = {1, 2, 3}
b = {3, 4, 5}

a.add(6)               # Adds element to set 'a'
a.remove(2)            # Removes element 2 from set 'a'
a.discard(10)          # Removes 10 if present, else does nothing
a.pop()                # Removes and returns an arbitrary element
a.clear()              # Removes all elements from the set

a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))      # {1, 2, 3, 4, 5}
print(a.intersection(b))  # {3}
print(a.difference(b))    # {1, 2}
print(a.symmetric_difference(b))  # {1, 2, 4, 5}
