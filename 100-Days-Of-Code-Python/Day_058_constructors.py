# Class and Objects:

# Example 1:

class Person:
    
    def __init__(self, name, occupation, salary):
        self.name = name
        self.occupation = occupation
        self.salary = salary

    def info(self):
        print(f"{self.name} is a {self.occupation} and his salary is {self.salary}")
              
a = Person("Faizan", "Marketer", 150000)
b = Person("Ahmad", "HR", 200000)
c = Person("Aftab", "Programmer", 125000)

a.info()
b.info()
c.info()