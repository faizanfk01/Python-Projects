# Operations in Tuples:

my_tuple = (10, 20, 30, 20, 40)

count_20 = my_tuple.count(20)   # Counts occurrences of 20 → 2
index_30 = my_tuple.index(30)   # Finds index of first 30 → 2

# Basic tuple operations
length = len(my_tuple)                # Length of the tuple → 5
exists = 40 in my_tuple               # Check if 40 exists → True
concatenated = my_tuple + (50, 60)   # Concatenate tuples → (10, 20, 30, 20, 40, 50, 60)
repeated = my_tuple * 2              # Repeat tuple → (10, 20, 30, 20, 40, 10, 20, 30, 20, 40)

# Tuple unpacking
a, b, c, d, e = my_tuple              # Unpacks values into variables

# Outputs for reference
print("Tuple:", my_tuple)
print("Count of 20:", count_20)
print("Index of 30:", index_30)
print("Length:", length)
print("Exists 40?:", exists)
print("Concatenated:", concatenated)
print("Repeated:", repeated)
print("Unpacked values:", a, b, c, d, e)