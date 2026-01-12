class Employee:
    company_name = "One Roof AutoCare"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def info(self):
        print(f"The name of the employee is {self.name} his salary is {self.salary}, the company is {self.company_name}")
    
    @classmethod
    def changecompany(cls, new_company):
        cls.company_name = new_company

emp = Employee("Faizan", 120000)
# emp.changecompany("Abasfhnasjkfb")
emp.info()

emp1 = Employee("Shahab Khan", 200000)
emp1.changecompany("Abasfhnasjkfb")
emp1.info()
print(Employee.company_name)