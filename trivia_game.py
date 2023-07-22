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
# https://opentdb.com/api.php?amount=10&category=12&difficulty=easy
# https://opentdb.com/api.php?amount=10
response_API_trivia_questions = requests.get('https://opentdb.com/api.php?amount=20&category=12&difficulty=easy')
# print(response_API.status_code)

data = response_API_trivia_questions.text

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

    def __init__(self, name, score = 0, incorrect_answers = 0):
        self.name = name 
        self.score = score
        self.incorrect_answers = incorrect_answers
 

class Trivia:

    @staticmethod
    def play_game():
        Question.create_questions(data)
        num_of_questions = len(Question.question_library)

        print('Player 1 enter your name\n')
        name = input()
        player_1 = Player(name)
        print(f'Welcome {player_1.name}\n')

        print('Player 2 enter your name\n')
        name = input()
        player_2 = Player(name)
        print(f'Welcome {player_2.name}\n')

        user = ''
        while Question.question_library:
            if user == player_1:
                user = player_2  
            else: 
                user = player_1
            
            print('Question #', num_of_questions)
            num_of_questions -= 1
            Trivia.ask_question(user)
        
        if player_1.score > player_2.score:
            winner = player_1
        else:
            winner = player_2

        print('You won', winner.name)
        print('with a score of', winner.score)


    def ask_question(user):
        game_question = choice(Question.question_library)
        Question.question_library.remove(game_question)

        print(user.name)
        print(game_question.question)

        answer = game_question.correct_answer
        wrong_answers = game_question.incorrect_answers
        choice_keys = ['D', 'C', 'B', 'A']
        choice_dict = {}
        answers = [*wrong_answers, answer]
        
        while answers:
            ans = choice(answers)
            choice_letter = choice_keys.pop()
            print(f'{choice_letter}. {html.unescape(ans)}')
            choice_dict[choice_letter] = ans
            answers.remove(ans)

        user_selection = input('Your guess:  ')
        if choice_dict[user_selection] == answer:
            print('Correct\n')
            user.score += 1
        else:
            print('Incorrect, the answer is:', answer)
            user.incorrect_answers += 1
            print(' ')

Trivia.play_game()
