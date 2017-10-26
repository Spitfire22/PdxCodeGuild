
'''

A cheesy version of Fifth Element Game as Adventure.

Note to Allen:
structure your classes as levels & transitions including transitions which
can end the game if the user doesn't guess properly. Give each wrong guess
an added layer of gameplay instead of just ending, but all aspects of that
wrong level will lead to an end with some options being quicker than others.

Do a rolling intro where the user has to press enter to populate the next aspect
of the story.

While the game story is important for you to get right, getting a minimum
viable product is also important, so don't get hung up on just the detail
of the story but put forth some fillers on each of the story lines.

For later versions :
imagine at each major scene transition if something else
had happened. Like if the Chinese food cart guy takes the Fhloston tickets.
Or if Zorg actually chokes and dies.
Or if Leeloo stays with the government instead of escapes and you are just
driving around as a cabbie.
Make decsions as other characters, which ultimately influence you
playing as Corbin. Direct the game to the movie.

'''
from sys import exit
import random
from textwrap import dedent
import time


print('-'*60,'\n')
print('''``````````````````````````````````T H E  F I F T H  E L E M E N T ``````````````````````````````````
````````````````````````````````````````````````````````````````````````````````````````````````````
````````````````````````````````````````````````````````````````````````````````````````````````````
````````````````````````````````````````````````````````````````````````````````````````````````````
````````````````````````````````````````````.-:/++++/-``````````````````````````````````````````````
````````````````````````````````````````-:/++++++++++++:.```````````````````````````````````````````
``````````````````````````````````````.++++++++++++++++++:.`````````````````````````````````````````
`````````````````````````````````````-+o+++++++++++++++++++-````````````````````````````````````````
````````````````````````````````````.+++++++++++++++++++++++/.``````````````````````````````````````
````````````````````````````````````-++++++++++/++++++++++++++.`````````````````````````````````````
````````````````````````````````````/++++++:::/.-++++++++++++o+.````````````````````````````````````
````````````````````````````````````+o++..-`.````...-+++++++++++.```````````````````````````````````
````````````````````````````````````++o/`````````````-++++++++++/```````````````````````````````````
```````````````````````````````````.o+o+:`````````````+++++++++++-``````````````````````````````````
```````````````````````````````````.o++o+`````````````+++++++++++:``````````````````````````````````
```````````````````````````````````-++++o:```````````.+++++++++++:``````````````````````````````````
```````````````````````````````````.o+++++-``````````:+++++++++++.``````````````````````````````````
````````````````````````````````````+++++++:`````````+o+++++++++-```````````````````````````````````
````````````````````````````````````/+++++++:```````-+++++++/-.-````````````````````````````````````
````````````````````````````````````-+++++/:::.`````++++/:..````````````````````````````````````````
`````````````````````````````````````:+++:``````````::-.````````-:/:-.``````````````````````````````
``````````````````````````````````````:/-`````.``````````````.://-.`````````````````````````````````
``````````````````````````````````````````.-::.````````````./+/.````````````````````````````````````
````````````````````````````````````````-/+/.````````````-/++:``````````````````````````````````````
```````````````````````````````````````:+/-````````````./+/+/```````````````````````````````````````
``````````````````````````````````````:++.````````````:++//+.```````````````````````````````````````
`````````````````````````````````````.+/.````````````/+++o+-````````````````````````````````````````
````````````````````````````````````.+:`````````````//--:+/`````````````````````````````````````````
```````````````````````````````````-/-`````````````/+-``-+-`````````````````````````````````````````
``````````````````````````````````:/.`````````````:++++++o``````````````````````````````````````````
`````````````````````````````````-/``````````````.+++++++o.`````````````````````````````````````````
`````````````````````````````````+-``````````````:++:-:+oo:`````````````````````````````````````````
````````````````````````````````.o:``````````````/+:```:oo+`````````````````````````````````````````
````````````````````````````````.++.`````````````+++-.-+o++:````````````````````````````````````````
`````````````````````````````````/++.````````````o++++++++++.```````````````````````````````````````
`````````````````````````````````-++/```````````.o+++++/+++++.``````````````````````````````````````
``````````````````````````````````++/```````````.o+o+-```/o+++-`````````````````````````````````````
``````````````````````````````````-++```````````.++++````/+++o+:````````````````````````````````````
```````````````````````````````````++/-`````````.o+++/::++oo+/-+/```````````````````````````````````
```````````````````````````````````/++/`````````.o++++++++/::/++/```````````````````````````````````
```````````````````````````````````-+++`````````-o+++++++.````.//```````````````````````````````````
````````````````````````````````````++-`````````-++//+++-```````.```````````````````````````````````
````````````````````````````````````/+/`````````:+.``.+:````````````````````````````````````````````
````````````````````````````````````:++`````````:+/--/+`````````````````````````````````````````````
````````````````````````````````````.o+`````````++++++-`````````````````````````````````````````````
`````````````````````````````````````o+````````.+++++:``````````````````````````````````````````````
`````````````````````````````````````++````````//:/+/```````````````````````````````````````````````
`````````````````````````````````````/o.``````.+-`-+.```````````````````````````````````````````````
`````````````````````````````````````:+:``````/++++:````````````````````````````````````````````````
`````````````````````````````````````-++`````.+o+++`````````````````````````````````````````````````
``````````````````````````````````````++-````:++oo/`````````````````````````````````````````````````
``````````````````````````````````````:++````/+.++-`````````````````````````````````````````````````
```````````````````````````````````````/+:```++/++``````````````````````````````````````````````````
```````````````````````````````````````.++-``++++/``````````````````````````````````````````````````
````````````````````````````````````````-++-`++++/``````````````````````````````````````````````````
`````````````````````````````````````````-++/o+/++``````````````````````````````````````````````````
``````````````````````````````````````````-+++++++.`````````````````````````````````````````````````
```````````````````````````````````````````./+++++:`````````````````````````````````````````````````
`````````````````````````````````````````````.:/+++.````````````````````````````````````````````````
````````````````````````````````````````````````..-.````````````````````````````````````````````````
````````````````````````````````````````````````````````````````````````````````````````````````````
````````````````````````````````````````````````````````````````````````````````````````````````````
````````````````````````````````````````````````````````````````````````````````````````````````````
````````````````````````````````````````````````````````````````````````````````````````````````````
````````````````````````````````````````````````````````````````````````````````````````````````````''')
print('-'*60,'\n')


#insert apartment() pick up items HP potion, pants, gun , jacket.


def player_haaa():

    def __init__(self, health, attack, armor, ammo, items):
        self.health = health
        self.attack = attack
        self.armor = armor
        self.ammo = ammo
        self.items = items


# player_haaa is health: | attack strength: | armor: | ammo:
# can add health when found food, medicine, or alcohol, if HP = 100, add to items.
# increases attack strength when 3 enemies are killed, or when a new weapon is found. older weapons are less attack.
# armor increases when items are found.
# ammo is added after each battle, each enemy char increases specified ammo.


'''

following are game boards through all of the scenes.

'''

class death(scene):

    quips = ['Man, Zorg is gonna be happy to hear this. Evil prevails again...',
             'Well, you can always use the Life-Rehabilitator 9000! Just kidding, it doesn\'t exist',
             'Where is it that you go once you die in this world? Are cemetaries such a thing?',
             'Everything gets enveloped by an evil black little star, or is it a planet? Good going Corbin...',
             'You should give this game to a smarter friend, we can only go through this so many times...',
             'Hear that noise? ... rather the lack of noise? Its the sound of GAME OVER.',
             'Bad guys prevail, Good guys make dumb decisions. Why is that always the case?'
             'Oh, you died.                      AGAIN.']

    def enter(self):
        print(death.quips[random.randint(0, len(self.quips)-1)])
        exit(1)


class corbin_apartment(scene):

    def main():
        pass

    def enter(self):
        print('Apartment scene')
        print('This scene is not yet configured, Zorg apologizes for the convience of destroying your world.')

        action = input('Answer the door? Damn it, yeah or nah...').lower()
        if action in ('yeah', 'damn it, yeah', 'damn', 'yes', 'yah', 'answer', 'open'):
            print('You opened the door and stuff happened')

        if action in ('nah', 'nope', 'no', 'no way'):
            print('This really complex scene happens where the rest of the world falls against Zorg and the Great Evil')
            return 'death'



class get_away(scene):

    def enter(self):
        print('Avoiding the police')
        print('This scene is not yet configured, Zorg apologizes for the convience of destroying your world.')

class cornelius_apartment(scene):

    def enter(self):
        print('Meeting Cornelius')
        print('This scene is not yet configured, Zorg apologizes for the convience of destroying your world.')

class space_port(scene):

    def enter(self):
        print('Space port - Multipass')
        print('This scene is not yet configured, Zorg apologizes for the convience of destroying your world.')

class space_ship(scene):

    def enter(self):
        print('On the ship to Fhloston Paradise')
        print('This scene is not yet configured, Zorg apologizes for the convience of destroying your world.')
        #scene 1 - boarding ship
        #scene 2 - Leeloo hotel room
        #scene 3 - opera
        #scene 4 - ballroom battle

class egypt(scene):

    def enter(self):
        print('Enter the pyramid - set up the stones in the correct order')
        print('This scene is not yet configured, Zorg apologizes for the convience of destroying your world.')
        # use time dialation - space time moved slower


class map(object):
    scene_transition = {
        'corbin apartment': corbin_apartment(),
        'get away': get_away(),
        'cornelius apartment': cornelius_apartment(),
        'space port': space_port(),
        'space ship': space_ship(),
        'egypt': egypt()
    }



width = 20  # the width of the board
height = 20  # the height of the board

# create a board with the given width and height
# we'll use a list of list to represent the board
board = []  # start with an empty list
for i in range(height):  # loop over the rows
    board.append([])  # append an empty row
    for j in range(width):  # loop over the columns
        board[i].append(' ')  # append an empty space to the board



'''


'''
# use this for full size boards NVM doesnt work
# def player_loc():
#     # define the player position
#     player_i = 4
#     player_j = 4


'''
Following are functions per the scenes through the game

'''
year = '2234'
def asleep():
    print('Your eyes are getting heavy and your body is feeling lethargic.\n'
          'the sounds around you fade away and your body becomes numb\n'
          'Life is over for you Corbin')
    end()

timeline = {
    1: {'time': '9:37 am, June 3rd, - Current Earth Time'}, # corbin wakeup - Scene transition only
    2: {'time': '10:04 am, June 3rd, - Current Earth Time'}, # corbin walkaround apartment - game play
    3: {'time': '11:40 am, June 3rd - Current Earth Time'}, # get away - game play
    4: {'time': '3:18 pm, June 3rd - Current Earth Time'}, # cornelius apartment - game play
    5: {'time': '10:40 am, June 4th - Current Earth Time'}, # space port - game play
    6: {'time': '11:00 am, June 4th- Current Adjusted Earth Time'}, # boarding ship - scene transition only
    7: {'time': '2:00 pm, June 4th - Current Adjusted Earth Time'}, # Leeloo room scene - game play
    8: {'time': '5:00 pm, June 4th - Current Adjusted Earth Time'}, # Opera scene - game play
    9: {'time': '5:35 pm, June 4th - Current Adjusted Earth Time'}, # Ballroom battle - game play
    10: {'time': '6:20pm, June 4th - Current Adjusted Earth Time'}, # Flight back to Earth - Scene transition
    11: {'time': '7:08 am, June 5th'}, #Egypt scene arranging blocks - game play
    }



time_stamp = timeline[1]['time']

def end():
    print('Location: Box | ')

# add 4 enemies in random locations
for i in range(4):
    enemy_i = random.randint(0, height - 1)
    enemy_j = random.randint(0, width - 1)
    board[enemy_i][enemy_j] = '§'



def location():
    # define the player position
    player_i = 8
    player_j = 8
    # loop until the user says 'done' or dies
    while True:

        command = input('what is your command? ')  # get the command from the user

        if command == 'done':
            break  # exit the game
        elif command == 'left':
            player_j -= 1  # move left
        elif command == 'right':
            player_j += 1  # move right
        elif command == 'up':
            player_i -= 1  # move up
        elif command == 'down':
            player_i += 1  # move down

        # check if the player is on the same space as an enemy
        if board[player_i][player_j] == '§':
            print('You\'ve encountered an enemy!')
            action = input('what will you do? ')
            if action == 'attack':
                print('you\'ve slain the enemy')
                board[player_i][player_j] = ' '  # remove the enemy from the board
            else:
                print('you hestitated and were slain')
                break

                # print out the board
        for i in range(height):
            for j in range(width):
                # if we're at the player location, print the player icon
                if i == player_i and j == player_j:
                    print('ͼ', end=' ')
                else:
                    print(board[i][j], end=' ')  # otherwise print the board square
            print()
# location()

time.sleep(10)
print(dedent('''
    \tThe year is 2263.\n
    A 'Great Evil' appears in the form of a firey planet.
    Unprovoked the evil planet obliterates a fleet of space craft tasked with investigating the 
    new arriving planet.
    On earth, the world's president consults with his military and science
    advisers about the approaching planetoid.
    Arrogantly they fire upon it - making it larger.

    \t\t\tSoon, the 'Great Evil' will consume earth. 
    '''))
time.sleep(10)
print('-' * 60, '\n')
print('Location: Apartment | ', timeline[1]['time'], year,' | Mood: Apathetic')

time.sleep(7)
print(dedent('''    
    \tGood Morning Corbin Dallas!
    You have one point left on your license.
    Please drive safely today!

You grumble when the door buzzes.
'''))


