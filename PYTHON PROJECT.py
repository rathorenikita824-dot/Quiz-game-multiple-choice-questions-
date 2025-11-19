questions = [
    {
        "q": "1) Which keyword is used to define a function in Python?",
        "options": ["A. func", "B. def", "C. create", "D. function"],
        "answer": "B"
    },
    {
        "q": "2) Which method adds an element to the end of a list?",
        "options": ["A. add()", "B. insert()", "C. append()", "D. push()"],
        "answer": "C"
    },
    {
        "q": "3) True/False values in Python belong to which data type?",
        "options": ["A. int", "B. str", "C. bool", "D. float"],
        "answer": "C"
    },
    {
        "q": "4) Which operator is used for integer (floor) division?",
        "options": ["A. /", "B. //", "C. %", "D. **"],
        "answer": "B"
    },
    {
        "q": "5) What is the output of len([10, 20, 30])?",
        "options": ["A. 2", "B. 3", "C. 4", "D. Error"],
        "answer": "B"
    },
    {
        "q": "6) What is used for exception handling in Python?",
        "options": ["A. try/except", "B. if/else", "C. loop", "D. switch"],
        "answer": "A"
    }
]

score = 0

print("\n===== PYTHON QUIZ GAME =====\n")

for q in questions:
    print(q["q"])
    for opt in q["options"]:
        print(opt)
    user_ans = input("Enter your answer (A/B/C/D): ").upper()

    if user_ans == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print("Wrong!\n")

print("===== RESULT =====")
print(f"Your Score: {score} / {len(questions)}")
print(f"Percentage: {(score/len(questions))*100:.2f}%")
