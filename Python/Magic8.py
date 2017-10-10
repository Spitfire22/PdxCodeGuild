import random

print('\tThis is the \n \tM * A * G * I * C \n\t8-BALL\n\n Ask your question and I will answer!\n')

result = ['It is certain', 'It is decidedly', 'Without a doubt', 'Yes definitely', 'You may rely on it']
result += ['As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes',]
result += ['Reply hazy, try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now']
result += ['Concentrate and ask again', 'Don\'t count on it', 'My reply is no', 'My sources say no']
result += ['Outlook not so good', 'Very doubtful']



shake = ""
while shake != "done" :
    query = input('I need to know if you want to \'shake\' or if you\'re \'done\': ')
    if query == 'shake':
        question = input('What question do you want me to answer? ')
        results = random.choice(result)
        print(results)
    elif query == 'done':
        quit()

else :
    print("Thanks for playing!")