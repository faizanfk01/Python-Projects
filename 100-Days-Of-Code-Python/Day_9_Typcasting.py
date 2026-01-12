# Type Casting is the process of converting one data type to another.
# Type Casting in Python can be done in two ways: Implicit Conversion and Explicit Conversion.

# Implicit Conversion:
# Implicit Conversion happens automatically when Python converts one data type to another without any explicit instruction.
# Example: When you add an integer and a float, Python automatically converts the integer to a float.

# Implicit Conversion Example:

x = 10       # int
y = 5.5      # float

# Implicit conversion: Python automatically converts x to a float for the addition.

result = x + y
print(f"Implicit Conversion Result: {result}, Type: {type(result)}")

# Output: Implicit Conversion Result: 15.5, Type: <class 'float'>

# Explicit Conversion:

# Explicit Conversion is when you manually convert a value from one type to another using specific functions like int(), str(), or float().
# Example: Using int() to convert a string to an integer.

# Explicit Conversion Example:

x1 = 4        # string
y1 = "123"

result1 = x1 + int(y1)

print(f"Explicit Conversion Result: {result1}, Type: {type(x1)}")

# Output: Explicit Conversion Result: 127, Type: <class 'int'>