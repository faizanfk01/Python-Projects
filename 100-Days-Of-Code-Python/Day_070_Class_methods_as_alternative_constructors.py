class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def info(self):
        print(f"The name of the employee is {self.name} and his salary is {self.salary}")

    @classmethod
    def fromstr(cls, string):
        return cls(string.split("-")[0], int(string.split("-")[1]))
    
emp1 = Employee("Faizan", 500000)
emp1.info()

shahab = "Shahab Khan-300000"
emp2 = Employee.fromstr(shahab)
emp2.info()