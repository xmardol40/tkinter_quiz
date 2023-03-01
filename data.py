import requests

url = "https://opentdb.com/api.php?amount=10&type=boolean"

response = requests.get(url)
response.raise_for_status()
#print(response)
data = response.json()
question_data = data["results"]
#print(question_data)

question_list = []
answers_list = []

for one_question in question_data:
    question_t = one_question["question"]
    question_t = question_t.replace("&quot;", "´´")
    question_t = question_t.replace("&#039;", "´")
    question_a = one_question["correct_answer"]
    question_list.append(question_t)
    answers_list.append(question_a)