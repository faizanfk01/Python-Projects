# Example 1:

def add(a, b):
    return a + b

result = add(4, 5)
print(result)


# Example 2:

def greet(name="Faizan"):
    print(f"Hello, {name}")

greet()
greet("John")


# Example 3:

def multiply(*numbers):
    result = 1
    for num in numbers:
        result *= num
    print(f"The answer is: {result}")

multiply(2, 3, 4, 5, 6, 7, 8, 9, 10)


# Example 4:

def person(**names):
    for key, value in names.items():
        print(f"{key}: {value}")

person(name ="Faizan", age = 30, city = "Mardan")

# Example 5:

def name(*names):
    for name in names:
        print(name, end=" ")
    print("")

name("M.", "Faizan", "Khan", "III")
name("Dr.", "John", "William", "III")

