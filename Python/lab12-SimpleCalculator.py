'''
This is LAB 12 where we are making a simple calculator

'''
restart = "Y"
while restart == "Y":

    op = input('What is the operation you\'d like to preform? ')

    num1 = int(input('What is the first number? '))

    num2 = int(input('What is the second number? '))

    sol = ''
    if op == '+':
        sol = num1 + num2
    elif op == '-':
        sol = num1 - num2
    elif op == '*':
        sol = num1 * num2
    elif op == '/':
        sol = num1 / num2
    else :
        print('\nEither: Advanced functions not supported, or there was an error.')

    solution = print(num1, op, num2, ' = ', sol)

    restart = input('Whould you like to restart (Y/N) ? ')