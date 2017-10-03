import random

i = 0
numbers = []

eye = ['o O', 'x x', 'o -', '> <', 'q p', '* *', 'o-o']
nose = [' v ', ' u ', ' . ', ' ^ ']
mouth = [' - ' , ' _ ', ' & ', ' 0 ', ' U ']

while i < 5:
    eyes = random.choice(eye)
    noses = random.choice(nose)
    mouths = random.choice(mouth)


    print(eyes)
    print(noses)
    print(mouths)
    print('\n')

    i = i + 1
