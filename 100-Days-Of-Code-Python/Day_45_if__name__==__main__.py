# This condition ensures that code runs only when the script is executed directly.
# It prevents code from running during module import by checking if __name__ == "__main__".

def welcome():
    print("Hello you are welcome")


if __name__ == "__main__":
    welcome()