# Definition of shorthand if-else (ternary operator) in Python:
# It allows writing conditional statements in a single line.
# Syntax: value_if_true if condition else value_if_false

# Example 1
age = 17
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Minor

# Example 2
a, b = 15, 9
greater = a if a > b else b
print(greater)  # Output: 15

# Example 3
number = 7
parity = "Even" if number % 2 == 0 else "Odd"
print(parity)  # Output: Odd