from data import data
from question import Quiz
from quiz_brain import QuizBrain
from art import art

quiz_bank = []
for q in data:
    q_question = q["question"]
    q_answer = q['answer']
    new_question = Quiz(q_question, q_answer)
    quiz_bank.append(new_question)

quiz = QuizBrain(quiz_bank)
while quiz.still_has_questions():
    print(art)
    quiz.next_question()
else:
    print(f'Thank you for playing! Your score was: {quiz.score}/{quiz.quiz_number}')
