class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"\nQuestion {self.question_number}: {current_question.text} (True / False): ").lower()
        if answer == current_question.answer.lower():
            self.score += 1
            print("Correct!")
        else:
            print("Incorrect!")
            print(f"The correct answer was {current_question.answer}")
        print(f"Currect score: {self.score}/{self.question_number}")

    def still_has_questions(self):
        return self.question_number < len(self.question_list)



