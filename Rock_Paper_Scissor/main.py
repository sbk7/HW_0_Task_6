#Name: Saif Khan
'''
Date Created: 9/13/2022
The program below simulates a rock,paper,scissor game where the program,
will track the user and computers score.
'''

import random

#Initialize Global variables
user_score = 0
computer_score = 0

if __name__ == '__main__':


    options = ['rock', 'paper', 'scissor']

    while True:
        user_response = input("Enter Rock/Paper/Scissor or 'q' to quit: ").lower()

        # exits the Program
        if user_response == 'q':
            break #don't use quit() here


        if user_response not in options:
            continue #keep asking user if response is not correct

        random_num = random.randint(0,2)
        #Rock = 0 , Paper = 1, Scissor = 2

        computer_response = options[random_num].lower() #Computer decisions are random

        if user_response == computer_response:
            print(f'You chose {user_response.upper()} and Computer chose {computer_response.upper()}')
            print('This is a draw')
        elif user_response == 'rock' and computer_response == 'paper':
            print(f'You chose {user_response.upper()} and Computer chose {computer_response.upper()}')
            print('Computer Wins')
            computer_score +=1
        elif user_response == 'rock' and computer_response == 'scissor':
            print(f'You chose {user_response.upper()} and Computer chose {computer_response.upper()}')
            print('You Win')
            user_score +=1
        elif user_response == 'paper' and computer_response == 'scissor':
            print(f'You chose {user_response.upper()} and Computer chose {computer_response.upper()}')
            print('Computer Wins')
            computer_score +=1
        elif user_response == 'paper' and computer_response == 'rock':
            print(f'You chose {user_response.upper()} and Computer chose {computer_response.upper()}')
            print('You Win')
            user_score +=1
        elif user_response == 'scissor' and computer_response == 'rock':
            print(f'You chose {user_response.upper()} and Computer chose {computer_response.upper()}')
            print('Computer Wins')
            computer_score +=1
        elif user_response == 'scissor' and computer_response == 'paper':
            print(f'You chose {user_response.upper()} and Computer chose {computer_response.upper()}')
            print('You Win')
            user_score +=1

if user_score == 0 and computer_score == 0:
    print('Goodbye')
else:
    print(f'Your Score is {user_score} and Computer Score is {computer_score}')