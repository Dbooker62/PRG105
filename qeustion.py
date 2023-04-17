class Question:
    def __init__(self, question, answer1, answer2, answer3, answer4, correct_answer):
        self._question = question
        self._answer1 = answer1
        self._answer2 = answer2
        self._answer3 = answer3
        self._answer4 = answer4
        self._correct_answer = correct_answer

    def get_question(self):
        return self._question

    def get_answer1(self):
        return self._answer1

    def get_answer2(self):
        return self._answer2

    def get_answer3(self):
        return self._answer3

    def get_answer4(self):
        return self._answer4

    def get_correct_answer(self):
        return self._correct_answer

    def set_question(self, question):
        self._question = question

    def set_answer1(self, answer1):
        self._answer1 = answer1

    def set_answer2(self, answer2):
        self._answer2 = answer2

    def set_answer3(self, answer3):
        self._answer3 = answer3

    def set_answer4(self, answer4):
        self._answer4 = answer4

    def set_correct_answer(self, correct_answer):
        self._correct_answer = correct_answer


questions = [
    Question("What is the capital of France?", "Paris", "Berlin", "London", "Madrid", 1),
    Question("Which planet is closest to the Sun?", "Venus", "Mars", "Mercury", "Jupiter", 3),
    Question("What is the largest mammal?", "Elephant", "Blue Whale", "Giraffe", "Polar Bear", 2),
    Question("What is the chemical symbol for gold?", "Au", "Ag", "Fe", "Hg", 1),
    Question("What is the largest organ in the human body?", "Heart", "Lung", "Liver", "Skin", 4),
    Question("What is the tallest mountain in the world?", "Mount Kilimanjaro", "Mount Everest", "Mount Fuji",
             "Mount McKinley", 2),
    Question("What is the currency of Japan?", "Yen", "Dollar", "Euro", "Pound", 1),
    Question("Who painted the Mona Lisa?", "Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Michelangelo", 2),
    Question("What is the national flower of the United States?", "Rose", "Tulip", "Daisy", "Sunflower", 1),
    Question("What is the largest ocean on Earth?", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean",
             4)
]

player1_points = 0
player2_points = 0

for i in range(5):
    print("Round", i + 1)
    print("Player 1: ", questions[i].get_question())
    print("1. " + questions[i].get_answer1())
    print("2. " + questions[i].get_answer2())
    print("3. " + questions[i].get_answer3())
    print("4. " + questions[i].get_answer4())
    answer1 = int(input("Enter your answer (1-4): "))
    if answer1 == questions[i].get_correct_answer():
        print("Correct!")
        player1_points += 1
    else:

        print("Incorrect. The correct answer is:", questions[i].get_correct_answer())
    print("Player 1 points:", player1_points)
    print("Player 2: ", questions[i + 5].get_question())
    print("1. " + questions[i + 5].get_answer1())
    print("2. " + questions[i + 5].get_answer2())
    print("3. " + questions[i + 5].get_answer3())
    print("4. " + questions[i + 5].get_answer4())
    answer2 = int(input("Enter your answer (1-4): "))
    if answer2 == questions[i + 5].get_correct_answer():
        print("Correct!")
        player2_points += 1
    else:
        print("Incorrect. The correct answer is:", questions[i + 5].get_correct_answer())
    print("Player 2 points:", player2_points)

print("Player 1 total points:", player1_points)
print("Player 2 total points:", player2_points)
if player1_points > player2_points:
    print("Player 1 wins!")
elif player1_points < player2_points:
    print("Player 2 wins!")
else:
    print("It'satie!")
