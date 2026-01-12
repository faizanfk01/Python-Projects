# Class and Objects:

# Example 1:

class Person:
    
    name = "Faizan"
    occupation = "Marketer"
    salary = 150000

    def info(self):
        print(f"{self.name} is a {self.occupation} and his salary is {self.salary}")
              
a = Person()
b = Person()
c = Person()

b.name = "Ahmad"
b.occupation = "HR"
b.salary = 200000

c.name = "Aftab"
c.occupation = "Programmer"
c.salary = 125000

a.info()
b.info()
c.info()