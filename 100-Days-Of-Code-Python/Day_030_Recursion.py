# Recursion is a programming technique where a function calls itself.
# It solves a problem by breaking it into smaller instances of the same problem.

# Example 1: Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Example 2: Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Example 3: Sum of natural numbers
def sum_natural(n):
    if n == 1:
        return 1
    return n + sum_natural(n - 1)

# Example 4: Countdown
def countdown(n):
    if n == 0:
        print("Lift off!")
    else:
        print(n)
        countdown(n - 1)

print(factorial(5))
print(fibonacci(6))
print(sum_natural(10))
countdown(5)