# read(): Reads the entire content of the file as a single string.
# Returns everything from the current cursor position to the end of the file.

with open("sample.txt", "w") as f:
    f.write("Line1\nLine2\nLine3")

with open("sample.txt", "r") as f:
    content = f.read()
    print("read():\n", content)


# readline(): Reads the next line from the file, including the newline character.
# Each call to readline() reads one more line.

with open("sample.txt", "r") as f:
    print("readline():", f.readline(), end="")  # Line1
    print("readline():", f.readline(), end="")  # Line2


# readlines(): Reads all lines in a file and returns them as a list.
# Each list item is a line from the file, including the newline character.

with open("sample.txt", "r") as f:
    lines = f.readlines()
    print("readlines():", lines)


# write(): Writes a string to the file. Overwrites content in 'w' mode, appends in 'a' mode.
# You need to use file.write() manually for each string you want to write.

with open("sample.txt", "w") as f:
    f.write("New content\nAnother line")


# writelines(): Writes a list of strings to the file.
# Doesn't add newlines automatically — you must include '\n' manually if needed.

lines_to_write = ["Line A\n", "Line B\n", "Line C\n"]
with open("sample.txt", "w") as f:
    f.writelines(lines_to_write)

f = open("example.txt", "r")
while True:
    line = f.readline()
    if not line:
        break
    print(line)

# Example 1:

with open("info.txt", "w") as f:
    f.write("Name: Muhammad Faizan\nAge: 19")

with open("info.txt", "r") as f:
    text = f.read()
    print(text)


# Excercise 2:

with open("lines.txt", "w") as f:
    f.writelines("The cat danced on the rooftop under the silver moon.\nA broken clock is still right twice a day.\nSuddenly, the sky turned green and everyone cheered.\nI found a message in a bottle buried in the sand.\nBananas make terrible phones but excellent smoothies.")

with open("lines.txt", "r") as f:
    text = f.readlines()
print(len(text))


# Example 3:

with open("lines.txt", "r") as f:
    text = f.readline()
    print(text)


# Example 4:

fruits = ["Apple", "Banana", "Mango", "Orange", "Peach"]


with open("fruits.txt", "w") as f:
    f.writelines("Apple\nBanana\nMango\nOrange\nPeach")

with open("fruits.txt", "r") as f:
    text = f.readlines()
    for fruit in text:
        print(fruit.strip())


# Example 5:

with open("fruits.txt", "r") as f:
    text = f.read()
    print(text)

with open("backup.txt", "w") as f:
    f.write(text)