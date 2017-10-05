'''
This is madness!

No,
This is exercise 13.

*punt
'''
import random

print(' ' * 5, '-' * 25)
print('Welcome to the numbers guessing game!')
print(' ' * 5, '-' * 25)
print('''
You are going to try and guess the number I am thinking of.
Pretty easy right? Let's see how good you are!
''')
# end intro

i = 0
#while i < 10:

computer = random.randint(1, 10)

while True:

    nums = range(1, 11)
    print('Choose a number in this list:', list(nums))


    guess = int(input('What number are you thinking of? '))


    i = i + 1

    if guess != computer:
        if guess >= computer:
            print('Go lower!')
        if guess <= computer:
            print('Number is higher')
        #if guess == computer,
        #   print('That\'s right!')
        #print('The computer\'s number was ', computer)
        #if False:
        #if i != 10:
        #   print('You\'re on guess #:', i , 'Try again...')
        #if i == 10:
        #   print('You guessed too many times, Game over man! Game over!')

    elif guess == computer:
        print('Congrats! you guessed a total of ', i , ' times.', 'Your number guessed was: ', guess, ' and the computer guessed: ', computer, 'You Win!')
        break

    else :
        print('If you didn\'t want to play, shoulda just said so...')
        break






