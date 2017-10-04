cash = float(input('How much cash and change do you have? '))
print('We are going to convert that to coins only.')
quarter = (cash)//.25
print('That will take this many quarters:', quarter)
dimes = (cash)//.10
print('Including this many dimes:', dimes)
nickels = (cash)//.05
print('This amount of nickels:', nickels)
pennies = (cash)//.01
print('And this number of pennies:', pennies)

cash2 = int(input('\nGive me a number between 100 and 900: '))
penny = (cash2)//100
print('Here is a small bag of pennies equivalent of that value:')
print(float(cash2))