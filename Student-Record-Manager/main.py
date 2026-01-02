students = {
    1: ["Faizan", 20, "A"],
    2: ["Abbas", 18, "B"],
    3: ["Shahzaib", 17, "A"],
    4: ["Yaseen", 19, "C"],
    5: ["Abdullah", 21, "D"],
    6: ["Umar", 22, "A"]
}

find_student = int(input("Enter the student roll no (or press 7 to show all students): "))

if find_student in students:
    print(f"\nRoll No: {find_student}")
    print(f"Name : {students[find_student][0]}")
    print(f"Age : {students[find_student][1]}")
    print(f"Grade : {students[find_student][2]}\n")

elif find_student == 7:
    for student, details in students.items():
        print(f"\nRoll No. {student}")
        print(f"Name : {details[0]}")
        print(f"Age  : {details[1]}")
        print(f"Grade: {details[2]}")

else:
    print("No student in this roll no")