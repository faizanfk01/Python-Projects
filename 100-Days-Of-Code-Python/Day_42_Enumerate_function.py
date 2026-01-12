# Definition of enumerate() in Python:
# The enumerate() function adds a counter to an iterable and returns it as an enumerate object.
# Useful in loops when you need both index and value.

# Example 1
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
# Output:
# 0 apple
# 1 banana
# 2 cherry

# Example 2 (starting index from 1)
colors = ["red", "green", "blue"]
for i, color in enumerate(colors, start=1):
    print(f"{i}: {color}")
# Output:
# 1: red
# 2: green
# 3: blue