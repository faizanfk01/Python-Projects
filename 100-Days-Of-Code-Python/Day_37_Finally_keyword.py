# Finally:

def read_file(filename):
    try:
        file = open(filename, 'r')
        content = file.read()
        print("File content:")
        print(content)
    except FileNotFoundError:
        print("❌ File not found.")
    except PermissionError:
        print("❌ You do not have permission to read this file.")
    finally:
        # Ensures the file is closed whether an error occurs or not
        try:
            file.close()
            print("🔒 File closed safely.")
        except NameError:
            print("⚠️ File was never opened, nothing to close.")

# Call the function
read_file("example.txt")
