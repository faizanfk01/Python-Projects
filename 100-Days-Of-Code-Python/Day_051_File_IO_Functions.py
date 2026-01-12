# seek() Function:

# seek(offset): Moves the file pointer to the given byte position.
# seek(0) moves to the beginning, seek(10) moves to the 10th byte.

with open("example.txt", "r") as f:
    f.seek(6)
    text = f.read(6)
    print(text)


# tell() Function:

# tell(): Returns the current position of the file pointer in bytes.
# Helpful for tracking read/write progress.

with open("example.txt", "r") as f:
    f.seek(6)
    text = f.read(6)
    print(f.tell())
    print(text)


# truncate() Function:

# truncate(size): Trims the file to the given size (in bytes).
# If no size is given, it cuts from the current file pointer.

with open("example2.txt", "w") as f:
    f.write("Hello World!")
    f.truncate(5)

with open("example2.txt", "r") as f:
    print(f.read())