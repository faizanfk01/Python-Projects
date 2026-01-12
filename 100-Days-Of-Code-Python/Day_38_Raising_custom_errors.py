# Step 1: Define the custom exception
class InvalidAgeError(Exception):
    """Custom exception for invalid age values."""
    def __init__(self, age, message="Age must be between 0 and 120."):
        self.age = age
        self.message = message
        super().__init__(f"{message} You entered: {age}")


# Step 2: Function that raises the custom exception
def set_user_age(age):
    if not (0 <= age <= 120):
        raise InvalidAgeError(age)
    print(f"✅ Age set to: {age}")


# Step 3: Main program that handles the exception
def main():
    try:
        user_age = int(input("Enter your age: "))
        set_user_age(user_age)
    except InvalidAgeError as e:
        print("❌ Error:", e)
    except ValueError:
        print("❌ Please enter a valid number.")
    finally:
        print("✅ Age check complete.")

# Run the program
main()