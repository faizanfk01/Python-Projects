# Local Variable: Defined inside a function and accessible only within that function.
# It is created when the function starts and destroyed when the function ends.

def my_function():
    local_var = 10
    print("Local variable:", local_var)

my_function()
# print(local_var)  # Error: local_var is not accessible here


# Global Variable: Defined outside all functions and accessible throughout the code.
# Can be read from any function, but to modify it inside a function, use the 'global' keyword.

global_var = 20

def show_global():
    print("Global variable:", global_var)

def modify_global():
    global global_var
    global_var = 50

show_global()
modify_global()
show_global()