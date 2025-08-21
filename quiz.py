import time
from quiz_questions import general_knowledge_quiz

total_test_marks = 50
passing_marks = 25
student_marks = 0

choices = ["a", "b", "c", "d"]

for question, option in general_knowledge_quiz.items():
    print(f"\n{question}\na. {option['a']}\nb. {option['b']}\nc. {option['c']}\nd. {option['d']}")

    while True:
        choose_answer = input("Choose Your Answer (a, b, c, d): ").lower()

        if choose_answer in choices:
            if choose_answer == option['answer']:
                print(f"Correct! The Answer is: {choose_answer}")
                student_marks += 5
            else:
                print(f"Incorrect! The Answer is: {option['answer']}")
            break

        else:
            print("Incorrect choice, Please choose between (a, b, c, d)")

print("\nCalculating your score!")

time.sleep(2)

if student_marks >= passing_marks:
    print(f"\nCongrats You have passed the test\nYour Score is {student_marks} out of {total_test_marks}")
else:
    print(f"\nYou have failed the test\nYoue score is {student_marks} out of {total_test_marks}")