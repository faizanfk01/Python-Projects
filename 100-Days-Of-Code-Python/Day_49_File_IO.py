# File I/O: Used to read from or write to files using built-in functions like open(), read(), write(), etc.
# Python supports different file modes such as 'r' (read), 'w' (write), 'a' (append), and 'r+' (read/write).


# Reading a File:

f = open("example2.txt", "r")
text = f.read()
print(text)
f.close()

# Writing a File:

a = open("myfile.txt", "a")
a.write("Hello World!")
a.close()

# Best Way to open, read, write Files:

with open("file2.txt", "w") as f:
    f.write("Faizan is a good boy")

# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is a write example.\n")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print("File content:\n", content)

# Appending to a file
with open("example.txt", "a") as file:
    file.write("This is an appended line.\n")

# Reading again to show appended content
with open("example.txt", "r") as file:
    print("Updated content:\n", file.read())