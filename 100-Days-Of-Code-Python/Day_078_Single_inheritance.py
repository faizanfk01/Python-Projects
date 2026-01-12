# Single Inheritance:

class Employee:
    def __init__(self, name, salary, company):
        self.name = name
        self.salary = salary
        self.company = company

    def info(self):
        print(f"The Name of the employee is {self.name}, his salary is {self.salary}, the company is {self.company} ")

class Programmer(Employee):
    def __init__(self, name, salary, company, lang, id):
        super().__init__(name, salary, company)
        self.lang = lang
        self.id = id

    def prog_info(self):
        print(f"The name of the programmer is {self.name}, the salary is {self.salary}, he is {self.lang} developer his id is {self.id}")

programmer = Programmer("Faizan", 150000, "ABCD LTD", "Python", 24)
programmer.prog_info()
programmer.info()