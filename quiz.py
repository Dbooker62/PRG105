import random

numbers_dict = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten"
}


def start_quiz():
    total_questions = 10  # Total number of quiz questions
    correct_answers = 0  # To keep track of correct answers

    print("Welcome to the Number Quiz!")
    print("Translate the following numbers from the foreign language to English:")
    print("--------------------------------------------------------------")

    for i in range(total_questions):

        num = random.randint(1, 10)
        foreign_number = numbers_dict[num]

        print(f"What is '{foreign_number}' in English?")

        user_answer = input("Your Answer: ").lower().strip()
        if user_answer == numbers_dict[num]:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"Incorrect. The correct answer is '{numbers_dict[num]}'.")

    score = (correct_answers / total_questions) * 100
    letter_grade = ""
    if score >= 90:
        letter_grade = "A"
    elif score >= 80:
        letter_grade = "B"
    elif score >= 70:
        letter_grade = "C"
    elif score >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"

    print("--------------------------------------------------------------")
    print(f"You scored {correct_answers} out of {total_questions} questions correctly.")
    print(f"Your score is {score}%.")
    print(f"Letter Grade: {letter_grade}")


start_quiz()
