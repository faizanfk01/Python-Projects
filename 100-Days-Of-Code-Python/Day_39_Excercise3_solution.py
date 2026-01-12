# KBC-style Quiz Game

balance = 0

questions = [
    {
        "question": "Which planet is known as the Red Planet?",
        "options": {
            "a": "Earth",
            "b": "Mars",
            "c": "Jupiter",
            "d": "Saturn"
        },
        "answer": "b",
        "prize": 10000
    },
    {
        "question": "Who was the first Prime Minister of India?",
        "options": {
            "a": "Mahatma Gandhi",
            "b": "Jawaharlal Nehru",
            "c": "Sardar Patel",
            "d": "Lal Bahadur Shastri"
        },
        "answer": "b",
        "prize": 20000
    },
    {
        "question": "Which gas do plants absorb from the atmosphere?",
        "options": {
            "a": "Oxygen",
            "b": "Hydrogen",
            "c": "Carbon Dioxide",
            "d": "Nitrogen"
        },
        "answer": "c",
        "prize": 30000
    },
    {
        "question": "In which year did India gain independence?",
        "options": {
            "a": "1945",
            "b": "1946",
            "c": "1947",
            "d": "1948"
        },
        "answer": "c",
        "prize": 40000
    },
    {
        "question": "What is the capital of Australia?",
        "options": {
            "a": "Sydney",
            "b": "Melbourne",
            "c": "Canberra",
            "d": "Brisbane"
        },
        "answer": "c",
        "prize": 50000
    }
]

print("🎮 Welcome to KBC (Kaun Banega Crorepati)!")
print("Answer each question to win cash prizes!\n")

for index, q in enumerate(questions, start=1):
    print(f"Q{index}: {q['question']}")
    for key, value in q["options"].items():
        print(f"   {key.upper()}. {value}")
    
    answer = input("Your Answer (A, B, C or D): ").lower()
    
    if answer == q["answer"]:
        balance += q["prize"]
        print(f"✅ Correct! You've won Rs. {q['prize']}. Total Balance: Rs. {balance}\n")
    else:
        print(f"❌ Wrong answer. The correct answer was: {q['answer'].upper()}.")
        print(f"You leave with Rs. {balance}")
        break  # Ends the game on wrong answer

print("\n🏁 Game Over! Thank you for playing.")
print(f"💰 Your Final Balance: Rs. {balance}")