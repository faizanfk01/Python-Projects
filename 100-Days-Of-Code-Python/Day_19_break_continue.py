# Break Statement:

for number in range(1, 10):
    if number == 5:
        break
    print(number)

# # Continue Statement:

for number in range(1, 6):
    if number == 3:
        continue
    print(number)

# Example 1:

for i in range(1, 100):
    if i == 42:
        break
    print(i)


# Example 2:

for i in range(1, 20):
    if i % 3 == 0:
        continue
    print(i)


# Example 3:

word = input("Enter a word: ")
vowels = ["a", "e", "i", "o", "u"]

for l in word:
    if l.lower() in vowels:
        print("First vowel found:", l)
        break


# Example 4:

for i in range(1, 20):
    if i % 2 == 0:
        continue
    print(i)


# Example 5:

correct_password = "faizankhan123"

for attempt in range(3):
    password = input("Enter a password (3 attempts): ")

    if correct_password != password:
        print("Try again!")

    else:
        print("Acces Granted")
        break

else:
    print("You have been banned after 3 attempts")