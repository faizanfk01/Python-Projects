# A static method in Python is a method that does not access the instance (self) or class (cls).
# It is used for utility functions that are logically related to the class but do not need class or instance data.

class Math:
  def __init__(self, num):
    self.num = num

  def addtonum(self, n):
    self.num = self.num +n
    
  @staticmethod
  def add(a, b):
      return a + b

# result = Math.add(1, 2)
# print(result) # Output: 3
a = Math(5)
print(a.num)
a.addtonum(6)
print(a.num)

print(Math.add(7, 2)) 