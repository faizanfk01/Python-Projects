names = "Faizan, Ibrash"
print(names[0:6]) # String slicing.
print(len(names)) # we can find lenght of a string using len() function.

# Example of len().

fruit = "Apple"
len1 = len(fruit)
print("Apple is a", len1, "letter word")
print(fruit[:5]) # If we don't add 0 Python do it self.
print(fruit[0:5]) # If we add 0 the result will be same.
print(fruit[1:4]) # will start from the letter in the string.
print(fruit[0:-3]) # Negative Slicing.
print(fruit[-4:-1]) # Negative Slicing 2.