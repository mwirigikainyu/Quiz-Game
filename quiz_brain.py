class QuizBrain:
    def __init__(self, data):
        self.quiz_number = 0
        self.quiz_list = data
        self.score = 0

    def still_has_questions(self):
        return self.quiz_number < len(self.quiz_list)

    def next_question(self):
        current_question = self.quiz_list[self.quiz_number].question
        current_answer = self.quiz_list[self.quiz_number].answer
        self.quiz_number += 1
        my_answer = input(f"Q{self.quiz_number}: {current_question}(True/False)? ").lower()
        self.check_answer(my_answer, current_answer)

    def check_answer(self, my_answer, correct_answer):
        if my_answer == correct_answer.lower():
            self.score += 1
            print('✔️')
        else:
            print(f'❌ The correct answer was: {correct_answer}')
        print(f"Your current score is {self.score}/{self.quiz_number}\n")
