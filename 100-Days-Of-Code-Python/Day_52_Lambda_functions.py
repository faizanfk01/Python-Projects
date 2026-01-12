# Lambda Funtions:

# lambda: Creates a small, anonymous (unnamed) function in one line.
# Syntax: lambda arguments : expression

def apple(fx, value):
    return 6 + fx(value)

double = lambda x: x * 2
cube = lambda x: x * x * x
avg = lambda x, y, z: (x + y + z) / 3

print(double(5))
print(cube(5))
print(avg(3, 5, 10))
print(avg(3, 6, 4))
print(apple(lambda x: x * x * x, 2))