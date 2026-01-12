# Example 1:

def greet(name, greet):
    print(f"Hello {name}, You are {greet}")

greet("Faizan", "Welcome")


# Example 2:

def add(a, b):

    print(f"Addition of {a} + {b} is: {a + b}")

add(8, 7)


# Example 3:

def lenth(l):
    return len(l)

print(lenth("Faizan"))


# Example 4:

def even(a):
    return a % 2 == 0
    
print(even(8))
print(even(7))


# Example 5:

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))


# Example 6:

def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

print(count_vowels("Faizan"))
print(count_vowels("Ibrash"))    
print(count_vowels("AEIOU"))