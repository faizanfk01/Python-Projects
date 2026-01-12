# The os module provides a way to interact with the operating system's file and directory structure.
# It allows for tasks like path manipulation, file handling, and running system commands.

import os

os.name                     # Returns the name of the OS-dependent module imported ('posix', 'nt', etc.)
os.getcwd()                 # Returns the current working directory
os.chdir('path')            # Changes the current working directory to 'path'
os.listdir('path')          # Lists files and directories in the given path
os.mkdir('dirname')         # Creates a new directory named 'dirname'
os.makedirs('a/b/c')        # Creates nested directories (e.g., a/b/c)
os.remove('file.txt')       # Deletes the specified file
os.rmdir('dirname')         # Deletes the specified empty directory
os.removedirs('a/b/c')      # Deletes nested directories recursively if empty
os.path.exists('file.txt')  # Checks if a file or directory exists
os.path.isfile('file.txt')  # Checks if the path is a regular file
os.path.isdir('dirname')    # Checks if the path is a directory
os.path.join('dir', 'file') # Joins one or more path components intelligently
os.path.basename()      # Returns the final component of a pathname
os.path.dirname()       # Returns the directory name from a pathname
os.system('command')        # Executes the system command passed as a string
os.environ                  # A dictionary of the environment variables


# Example 1:

print(os.getcwd())  # e.g., C:\Users\YourName\Projects

print(os.listdir())  # ['file1.py', 'notes.txt', 'images', ...]

# Create a directory if it doesn't already exist

if not os.path.exists('test_dir'):
    os.mkdir('test_dir')
    print("Directory 'test_dir' created.")
else:
    print("Directory 'test_dir' already exists.")

# Change into the new directory

os.chdir('test_dir')
print("Now inside:", os.getcwd())

# Example 2:

if os.path.exists("example.txt") and os.path.isfile("example.txt"):
    print("example.txt exists and is a file.")
else:
    print("Not found")

if os.path.exists("test_dir") and os.path.isdir("test_dir"):
    print("test_dir exists and is a directory.")

else:
    print("Not found")

# Example 3:

try:
    with open("temp.txt", "r") as file:
        content = file.read()
        print("File Content:\n", content)
except FileNotFoundError:
    print("Error: 'temp.txt' not found. Please create the file first.")
    exit()

ask = input("Want to check if the file exists or delete it? (check/delete): ").lower()

if ask == "check":
    if os.path.exists("temp.txt"):
        print("✅ File Exists")
    else:
        print("❌ File does not exist")

elif ask == "delete":
    if os.path.exists("temp.txt"):
        os.remove("temp.txt")
        print("🗑️ File deleted")
    else:
        print("⚠️ File already deleted or not found")
else:
    print("❌ Invalid input")