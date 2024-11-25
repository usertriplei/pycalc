# Simple Python Quiz Game

# List of questions and answers
quiz = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is 5 + 7?", "answer": "12"},
    {"question": "What is the color of the sky on a clear day?", "answer": "Blue"},
    {"question": "Which programming language is this quiz written in?", "answer": "Python"},
    {"question": "How many days are in a week?", "answer": "7"},
]

# Instructions
print("Welcome to the Quiz Game!")
print("You will be asked 5 questions. Type your answers and press Enter.")
print("Let's start!\n")

# Initialize score
score = 0

# Loop through each question
for i, item in enumerate(quiz, start=1):
    print(f"Question {i}: {item['question']}")
    answer = input("Your answer: ").strip()

    # Check answer
    if answer.lower() == item['answer'].lower():
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer was: {item['answer']}\n")

# Final score
print(f"You finished the quiz! Your score is {score}/{len(quiz)}.")

# Feedback based on score
if score == len(quiz):
    print("Excellent! You got a perfect score!")
elif score >= len(quiz) // 2:
    print("Good job! Keep practicing to get even better.")
else:
    print("Don't worry! Practice makes perfect.")
