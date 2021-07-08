import requests, html
r = requests.get('https://opentdb.com/api.php?amount=10&difficulty=easy&type=boolean').json()['results']
data = []
for collection in r:
    quiz_data = {
        'question': collection['question'],
        'answer': collection['correct_answer']
    }
    quiz_data['question'] = html.unescape(quiz_data['question'])
    data.append(quiz_data)
