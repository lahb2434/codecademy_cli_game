# Trivia game
# 2 player
# players get asked random questions from a list of questions
# and try to answer questions getting score if correct
# 20 questions per game
# Objects: players
# Player has a score 
# player has a tally of correct and incorrect answers
# do we create a object for the question?
# does the question class take care of the questions?
# {'category': 'Politics',
#   'type': 'multiple',
#   'difficulty': 'easy',
#   'question': 'Whose 2016 presidential campaign slogan was &quot;Make America Great Again&quot;?',
#   'correct_answer': 'Donald Trump',
#   'incorrect_answers': ['Ted Cruz', 'Marco Rubio', 'Bernie Sanders']},

import requests
import json
import html
from random import choice

response_API_trivia_questions = requests.get('https://opentdb.com/api.php?amount=50')
# print(response_API.status_code)

data = response_API_trivia_questions.text

# print(html.unescape(json.loads(data)['results'][0]['question']))

class Question:
    question_library = []

    def __init__(self, category, question, correct_answer, incorrect_answers):
        self.category = category       
        self.question = html.unescape(question)
        self.correct_answer =  correct_answer  
        self.incorrect_answers = incorrect_answers
        Question.question_library.append(self)

    @staticmethod
    def create_questions(data):
        questions_data = json.loads(data)['results']
        for question in questions_data:
            Question(
                question['category'],
                question['question'],
                question['correct_answer'],
                question['incorrect_answers']
            )

class Player:

    def __init__(self, name, score = 0, correct_answers = 0, incorrect_answers = 0):
        self.name = name 
        self.score = score
        self.correct_answers = correct_answers
        self.incorrect_answers = incorrect_answers  

print('Player 1 enter your name')
name = input()
player_1 = Player(name)
print(player_1.name)