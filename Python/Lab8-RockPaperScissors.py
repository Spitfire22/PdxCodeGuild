import random

game = ['rock', 'paper', 'scissors']

player = input('rock, paper, or scissors? ')
computer = random.choice(game)
print('The computer chose:', computer)

if player == 'scissors':
    if computer == 'rock':
        print('You\'ve got smashed!')
    if computer == 'paper':
        print('You cut that paper and won!')
    if computer == 'scissors':
        print('It\'s a tie!')
elif player == 'rock':
    if computer == 'rock':
        print('It\'s a tie!')
    if computer == 'paper':
        print('You\'re wrapped up! Game over!')
    if computer == 'scissors':
        print('Bang! You won!')
elif player == 'paper':
    if computer == 'rock':
        print('You wrapped the rock! Winner!')
    if computer == 'paper':
        print('Stacks of paper make are a tie...')
    if computer == 'scissors':
        print('You\'re trimmed into small peices, loser!')
else :
    print('Cheater!')
