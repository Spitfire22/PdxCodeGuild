import random

selection = ['l', '1', '{', 't', ';', 'r', 'a', 'd', '3']
selection += ['|', ')', '(', 'p', '#', 'c', '?', '@', 'z']
selection += ['>', '6', '8', 'm', 'q', 'e', '4', ':', '+']

password = ''
i = 0
while i < 10:
    password += random.choice(selection)

    i = i + 1

print(password)
