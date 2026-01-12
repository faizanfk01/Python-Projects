# Access modifiers in Python are used to control the visibility of class attributes and methods.
# Python supports public, protected, and private access using naming conventions (_ and __).

class Employee:
    def __init__(self, name, salary):
        self.name = name              # Public
        self._department = "HR"       # Protected (by convention)
        self.__salary = salary        # Private (name mangling with __)

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Department: {self._department}")
        print(f"Salary: {self.__salary}")

    def get_salary(self):             # Public method to access private attribute
        return self.__salary

# Creating an object
e = Employee("Ahsan", 200000)

print("\n--- Accessing Attributes ---")
print("Public:", e.name)              # ✅ Public: Accessible anywhere
print("Protected:", e._department)    # ⚠️ Protected: Accessible, but use with caution
# print("Private:", e.__salary)       # ❌ Error: Can't access directly

print("Private via getter:", e.get_salary())       # ✅ Safe way to access private
print("Private (name mangled):", e._Employee__salary)  # ⚠️ Hacky but possible (not recommended)