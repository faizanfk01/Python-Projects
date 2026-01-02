from abc import ABC, abstractmethod
import random

class Animal(ABC):
    zoo_name = "The Python Zoo"

    def __init__(self, name, species):
        self.name = name
        self.species = species

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def eat(self):
        pass

class Lion(Animal):
    def __init__(self, name):
        super().__init__(name, "Lion")

    def make_sound(self):
        print(f"{self.name} says: Roar!")

    def eat(self):
        print(f"{self.name} eats a large piece of meat!")

class Monkey(Animal):
    def __init__(self, name):
        super().__init__(name, "Monkey")

    def make_sound(self):
        print(f"{self.name} says: Ooh ooh aah aah!")

    def eat(self):
        print(f"{self.name} peels and eats a banana")

class ZooKeeper:
    def __init__(self, name):
        self.name = name
        self._employee_id = random.randint(1000, 9999)
        self.__salary = 45000

    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self.__salary = value


animals = [Lion("Lio"), Monkey("Momo")]
zookeeper = ZooKeeper("Hamza")

print(f"\nWelcome to {Animal.zoo_name}!")
print(f"\nEmployee ID of zoo keeper {zookeeper.name} is: {zookeeper._employee_id}")
print(f"Salary of {zookeeper.name} was: {zookeeper._ZooKeeper__salary}")
zookeeper.salary = 55000
print(f"Updated Salary of {zookeeper.name} is: {zookeeper.salary}\n")

for animal in animals:
    animal.make_sound()
    animal.eat()
    print(f"{animal.name} lives at {animal.zoo_name}\n")