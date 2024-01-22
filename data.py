import requests
parameters ={
    "amount":10,
    "type":"boolean",
    "category":18
}
response = requests.get(url="https://opentdb.com/api.php",params=parameters)
response.raise_for_status()
data= response.json()
question_data = data['results']

# question_data = {
# #     "question" : data['results'][0]['question'],
# #     "incorrect" : data['results'][0]['incorrect_answers'][0],
# #     "correct": data['results'][0]['correct_answer']
# # }
#
# question_data = {"question" :i['results'][0]['question'] for  in data}
# print(question_data)