from question_model import Question
from data import question_data, logo
from quiz_brain import QuizBrain
question_bank = []

for index in range(0, len(question_data)):
    new_q_answer = question_data[index]["correct_answer"]
    new_q_text = question_data[index]["question"]
    new_q = Question(new_q_text, new_q_answer)
    question_bank.append(new_q)
    
category = question_data[0]["category"]
difficulty = question_data[0]["difficulty"].capitalize()

print(f"{logo}")

print(f"Welcome to quiz.\nCategory: {category}\nDifficulty: {difficulty}")

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You have competed the quiz")
print(f"Your final score was: {quiz.user_score}/{quiz.question_number}")
