from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    text = question['text']
    answer =question['answer']
    question_object =Question(text, answer)
    question_bank.append(question_object)

#print(question_bank[0].answer)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

quiz_brain.final_score()
