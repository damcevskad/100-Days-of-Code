from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ascii_art import logo

question_bank = []

for question in question_data:
    new_question = Question(question["question"], question["correct_answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
print(logo)
while quiz.still_has_questions():
    quiz.next_question()
print("\nQuiz completed.")
print(f"Final score: {quiz.score}/{quiz.question_number}")
