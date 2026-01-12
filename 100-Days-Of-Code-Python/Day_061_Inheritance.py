# Inheritance:

class Employee:
    def __init__(self, name, occupation, salary, id):
        self.name = name
        self.occupation = occupation
        self.salary = salary
        self.id = id
        
    def info(self):
        print(f"The details of Employee {self.id} are: {self.name} is {self.occupation} and his/her salary is {self.salary}")

class Programmer(Employee):
    def __init__(self, name, occupation, salary, id, language, experience):
        super().__init__(name, occupation, salary, id)
        self.language = language
        self.experience = experience

    def prog_info(self):
        print(f"The Details of Programmer {self.id} are: {self.name} is {self.occupation} developer his/her salary is {self.salary} he/she has {self.experience} Years of experience in {self.language}")

# Employee Class:
a1 = Employee("Faizan", "Marketer", 200000, 291)
a2 = Employee("Ibrash", "HR", 250000, 203)
a3 = Employee("Danyal", "Manager", 220000, 209)
a4 = Employee("Fahad", "Incharge", 300000, 250)

# Programmer Class:

b1 = Programmer("Hashir", "Python", 150000, 313, "Python", 4)
b2 = Programmer("Abrar", "Java", 120000, 302, "Java", 6)
b3 = Programmer("Abdullah", "HTML", 170000, 322, "HTML", 3)
b4 = Programmer("Abaseen", "CSS", 145000, 363, "CSS", 5)

ask = input("Generate Details of Employees or Programmers?: ").lower()

if "employee" in ask:
    # Employee Info:
    a1.info()
    a2.info()
    a3.info()
    a4.info()

elif "programmer" in ask:
    # Programmer Info:
    b1.prog_info()
    b2.prog_info()
    b3.prog_info()
    b4.prog_info()

else:
    print("Invalid Input")