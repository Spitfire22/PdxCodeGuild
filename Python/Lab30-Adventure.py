
'''

A cheesy version of Fifth Element Game as Adventure.

'''

import random
from textwrap import dedent


print('-'*60,'\n')
print('\tFifth Element\t\n')
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

class scene_transition(object):

    def enter(self):
        print('This scene is not yet configured, Zorg apologizes for the convience of destroying your world.')

class corbin_apartment(scene_transition):

    def enter(self):
        print('Apartment scene')


class get_away(scene_transition):

    def enter(self):
        print('Avoiding the police')

class cornelius_apartment(scene_transition):

    def enter(self):
        print('Meeting Cornelius')

class space_port(scene_transition):

    def enter(self):
        print('Space port - Multipass')

class space_ship(scene_transition):

    def enter(self):
        print('On the ship to Fhloston Paradise')
        #scene 1 - boarding ship
        #scene 2 - Leeloo hotel room
        #scene 3 - opera
        #scene 4 - ballroom battle

class egypt(scene_transition):

    def enter(self):
        print('Enter the pyramid - set up the stones in the correct order')
        # use time dialation - space time moved slower






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
print('-' * 60, '\n')
print('Location: Apartment | ', timeline[1]['time'], year,' | Mood: Apathetic')


print(dedent('''    
    \tGood Morning Corbin Dallas!
    You have one point left on your license.
    Please drive safely today!

You grumble when the door buzzes.
'''))


def main():
    while True:
        command = input('Alarm goes off, do you get out of bed or try to fall back asleep?\n\t').lower()
        if command in ['done', 'quit', 'exit']:
            break
        elif command in['fall', 'asleep','back']:
            retrieve_user()
        elif command == 'create':
            create_user()
        elif command == 'update':
            update_user()
        elif command == 'delete':
            delete_user()
        else:
            print('command not recognized')