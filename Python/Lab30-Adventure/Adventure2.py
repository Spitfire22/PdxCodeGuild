'''

This is the main file of the game. populates player location and enemy locations.

'''


from World import World
from Entities import Corbin, Mangalore, Leeloo
from Scenes import Map, Engine, Opening, Death, CorbinApartment, GetAway, CorneliusApartment, SpacePort, SpaceShip, Egypt, Finished

a_map = Map('corbin apartment')
a_game = Engine(a_map)
world = a_game.play(Opening())

# can I import specific sizing from World?
# world = World(20, 10)

player_i, player_j = world.random_location()
player = Corbin(player_i, player_j)
world.entities.append(player)

# can I import specific # of enemies from World?
# also, can I import different enemies from Entites?
for i in range(10):
    mangalore_i, mangalore_j = world.random_location()
    mangalore = Mangalore(mangalore_i, mangalore_j)
    world.entities.append(mangalore)


while True:
    world.draw()
    command = input('what is your command? ').lower()
    if command in ['done', 'quit', 'exit']:
        break
    if command in ['l', 'left', 'w', 'west']:
        player.loc_i -= 1
    elif command in ['r', 'right', 'e', 'east']:
        player.loc_i += 1
    elif command in ['u', 'up', 'n', 'north']:
        player.loc_j -= 1
    elif command in ['d', 'down', 's', 'south']:
        player.loc_j += 1
    else:
        print('command not recognized')

    # if world is finished:
    #     get scene
    #     world = engine.run(scene)
    #     world.load()


    # check if the player is on the same space as an enemy
    # if board[player_i][player_j] == '§':
    #     print('You\'ve encountered an enemy!')
    #     action = input('what will you do? ')
    #     if action == 'attack':
    #         print('you\'ve slain the enemy')
    #         board[player_i][player_j] = ' '  # remove the enemy from the board
    #     else:
    #         print('you hestitated and were slain')
    #         break
    #
    #         # print out the board
    # for i in range(height):
    #     for j in range(width):
    #         # if we're at the player location, print the player icon
    #         if i == player_i and j == player_j:
    #             print('ͼ', end=' ')
    #         else:
    #             print(board[i][j], end=' ')  # otherwise print the board square
    #     print()
