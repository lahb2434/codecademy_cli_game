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


import requests
import json
import html
import os
from time import sleep
from random import choice
# https://opentdb.com/api.php?amount=10&category=12&difficulty=easy
# https://opentdb.com/api.php?amount=10
response_API_trivia_questions = requests.get('https://opentdb.com/api.php?amount=1&category=12&difficulty=hard')
# print(response_API.status_code)

data = response_API_trivia_questions.text

class Question:
    question_library = []

    def __init__(self, category, question, correct_answer, incorrect_answers):
        self.category = category       
        self.question = html.unescape(question)
        self.correct_answer =  html.unescape(correct_answer)  
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
    
    def winner(self, loser):
        print(self.name, 'won!' )
        print('with a score of', self.score)
        print(loser.name, 'lost!')
        print('with a score of', loser.score)
 

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

        sleep(0.5)
        os.system('clear')

        user = ''

        while Question.question_library:
            if user == player_1:
                user = player_2  
            else: 
                user = player_1
            
            print('Question #', num_of_questions)
            num_of_questions -= 1
            Trivia.ask_question(user)

        if player_1.score == player_2.score:
            print(f'Tied! with a score of {player_2.score}')
        elif player_1.score > player_2.score:
            player_1.winner(player_2)
        else:
            player_2.winner(player_1)

        
        while True:
            print('Play Again? Y/N')
            play_again = input().lower()
            if play_again == 'y':
                Trivia.play_game()
                break
            elif play_again == 'n':
                exit()


            


    def ask_question(user):
        game_question = choice(Question.question_library)
        Question.question_library.remove(game_question)

        print(user.name)
        print(game_question.question, '\n')

        answer = game_question.correct_answer
        wrong_answers = game_question.incorrect_answers
        choice_keys = ['d', 'c', 'b', 'a']
        choice_dict = {}
        answers = [*wrong_answers, answer]
        
        while answers:
            ans = choice(answers)
            choice_letter = choice_keys.pop()
            print(f'{choice_letter.upper()}. {html.unescape(ans)}')
            choice_dict[choice_letter] = ans
            answers.remove(ans)

        print('\n')
        user_selection = input('Your guess:  ').lower()
        while user_selection not in choice_dict:
            user_selection = input('Select from available choices:  ').lower()

        if choice_dict[user_selection] == answer:
            print('Correct\n')
            user.score += 1
        else:
            print('Incorrect, the answer is:', answer)
            user.incorrect_answers += 1
            print(' ')
        sleep(2)
        os.system('clear')

Trivia.play_game()
