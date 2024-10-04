import json

with open('quiz.json','r') as a:
    quiz_data = json.load(a)

quiz = quiz_data['quiz']


total_questions = 0
for category in quiz.values():
    total_questions += len(category)

print(f"Numero totale di domande: {total_questions}")


total_options = 0
total_questions_count = 0

for category in quiz.values():
    for question in category.values():
        total_options += len(question['options'])
        total_questions_count += 1

average_options = total_options / total_questions_count
print(f"Numero medio di risposte possibili: {average_options}")


math_questions = len(quiz.get('maths', {}))

print(f"Numero di domande di matematica: {math_questions}")