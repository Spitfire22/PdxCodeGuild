'''

These are the different scene transitions during the game once you get through
the game play of one level to the next.

'''
from sys import exit
from textwrap import dedent
import time
import random
from World import Apartment

class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)


def Opening():
    print('-' * 60, '\n')
    print('''\t``````````````````````````````````T H E  F I F T H  E L E M E N T ``````````````````````````````````
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
    ````````````````````````````````````````````````````````````````````````````````````````````````````''')
    print('-' * 60, '\n')
    time.sleep(5)
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
    return 'corbin apartment'


class Death(Scene):

    quips = ['\nMan, Zorg is gonna be happy to hear this. Evil prevails again...',
             '\nWell, you can always use the Life-Rehabilitator 9000! Just kidding, it doesn\'t exist',
             '\nWhere is it that you go once you die in this world? Are cemetaries such a thing?',
             '\nEverything gets enveloped by an evil black little star, or is it a planet? Good going Corbin...',
             '\nYou should give this game to a smarter friend, we can only go through this so many times...',
             '\nHear that noise? ... rather the lack of noise? Its the sound of GAME OVER.',
             '\nBad guys prevail, Good guys make dumb decisions. Why is that always the case?',
             '\nOh, you died.                      AGAIN.']

    def enter(self):
        print(Death.quips[random.randint(0, len(self.quips)-1)])
        exit(1)


class CorbinApartment(Scene):

    # def main():
    #     pass

    def enter(self):
        print('Apartment scene')
        print('This scene is not yet configured, Zorg apologizes for the convience of destroying your world.')
        action = input('Answer the door? \'Damn it, yeah\' or \'nah\'...').lower()
        if action in ('yeah', 'damn it, yeah', 'damn', 'yes', 'yah', 'answer', 'open'):
            print('You opened the door and stuff happened')
            return 'apartment'#'get away' # Map?

        if action in ('nah', 'nope', 'no', 'no way'):
            print('This really complex scene happens where the rest of the world falls against Zorg and the Great Evil')
            return 'death'



class GetAway(Scene):

    def enter(self):
        print('Leeloo dropped through your roof and you have no points left '
              'on your license. Good luck avoiding the police')
        print('This scene is not yet configured, Zorg apologizes for the convience of destroying your world.')
        exit(1)

class CorneliusApartment(Scene):

    def enter(self):
        print('Meeting Cornelius')
        print('This scene is not yet configured, Zorg apologizes for the convience of destroying your world.')
        exit(1)

class SpacePort(Scene):

    def enter(self):
        print('Space port - Multipass')
        print('This scene is not yet configured, Zorg apologizes for the convience of destroying your world.')
        exit(1)

class SpaceShip(Scene):

    def enter(self):
        print('On the ship to Fhloston Paradise')
        print('This scene is not yet configured, Zorg apologizes for the convience of destroying your world.')
        #scene 1 - boarding ship
        #scene 2 - Leeloo hotel room
        #scene 3 - opera
        #scene 4 - ballroom battle
        exit(1)

class Egypt(Scene):

    def enter(self):
        print('Enter the pyramid - set up the stones in the correct order')
        print('This scene is not yet configured, Zorg apologizes for the convience of destroying your world.')
        # use time dialation - space time moved slower
        exit(1)

class Finished(Scene):

    def enter(self):
        print('With your powers combined, you\'ve saved the planet!')


class Map(object):
    scene_transition = {
        'corbin apartment': CorbinApartment(),
        'apartment': Apartment(60, 10),
        'get away': GetAway(),
        'cornelius apartment': CorneliusApartment(),
        'space port': SpacePort(),
        'space ship': SpaceShip(),
        'egypt': Egypt(),
        'death': Death()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self,scene_name):
        val = Map.scene_transition.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map


    def play(self, current_scene):
        current_scene = self.scene_map.next_scene(current_scene)
        while isinstance(current_scene, Scene):
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        return current_scene