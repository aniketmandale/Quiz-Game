# Python quiz game

questions = ("What is Mahatma Gandhi called? ",
             "Name the 4th planet of our solar system? ",
             "Which animal can live without drinking water for many days? ",
             "What is National fruit of India? ",
             "Name one famous crop of Assam? ")  

options = (("A. National Son", "B. Father of Nation", "C. Son of Nation", "D. Father of India"),
           ("A. Venus", "B. Earth", "C. Mars", "D. Pluto"),
           ("A. Camel", "B. Lion", "C. Elephant", "D. Whale"),
           ("A. Banana", "B. Mango", "C. Grapes", "D. Apple"),
           ("A. Tobacco", "B. Cotton", "C. Jute", "D. Tea"))

answers = ("B", "C", "A", "B", "D")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")