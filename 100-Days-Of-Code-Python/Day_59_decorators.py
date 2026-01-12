# Decorators are functions that modify the behavior of other functions or methods.
# They allow for reusable, clean, and readable modifications using the @decorator_name syntax.

# 1. A simple decorator that logs before and after function execution
def simple_logger(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling '{func.__name__}'...")
        result = func(*args, **kwargs)
        print(f"[LOG] '{func.__name__}' finished.")
        return result
    return wrapper

@simple_logger
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")

# 2. A decorator for measuring execution time
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIMER] '{func.__name__}' took {end - start:.4f} seconds.")
        return result
    return wrapper

@timer
def compute():
    time.sleep(1)
    print("Computation complete.")

compute()

# 3. A decorator with arguments (parameterized decorator)
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hi there!")

greet()

# 4. Class method decorator: @staticmethod and @classmethod
class MyClass:
    @staticmethod
    def static_hello():
        print("Hello from static method.")

    @classmethod
    def class_hello(cls):
        print(f"Hello from class method in {cls.__name__}.")

MyClass.static_hello()
MyClass.class_hello()