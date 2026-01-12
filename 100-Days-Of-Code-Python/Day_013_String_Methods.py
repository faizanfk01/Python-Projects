# upper() - Converts all characters to uppercase (returns a new string).
print("hello".upper())  # Output: HELLO

# lower() - Converts all characters to lowercase.
print("HELLO".lower())  # Output: hello

# capitalize() - Capitalizes the first character and lowercases the rest.
print("hELLO world".capitalize())  # Output: Hello world

# title() - Capitalizes the first letter of each word.
print("hello world".title())  # Output: Hello World

# strip() - Removes leading and trailing whitespace or specified characters.
print("  hello  ".strip())  # Output: hello

# replace(old, new) - Replaces all occurrences of a substring with another.
print("banana".replace("a", "o"))  # Output: bonono

# split(separator) - Splits the string into a list using the separator.
print("a,b,c".split(","))  # Output: ['a', 'b', 'c']

# join(iterable) - Joins elements of an iterable with the string as separator.
print("-".join(["a", "b", "c"]))  # Output: a-b-c

# find(substring) - Returns the index of first occurrence of a substring or -1.
print("hello".find("l"))  # Output: 2

# count(substring) - Counts how many times a substring appears in the string.
print("banana".count("a"))  # Output: 3

# startswith(prefix) - Checks if the string starts with the given prefix.
print("hello".startswith("he"))  # Output: True

# endswith(suffix) - Checks if the string ends with the given suffix.
print("hello".endswith("lo"))  # Output: True

# isdigit() - Returns True if all characters in the string are digits.
print("12345".isdigit())  # Output: True

# isalpha() - Returns True if all characters are alphabetic.
print("abc".isalpha())  # Output: True

# isalnum() - Returns True if all characters are alphanumeric.
print("abc123".isalnum())  # Output: True