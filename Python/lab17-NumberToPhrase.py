
##['ten','twenty','thirty']
## put the numbers into a list and reference them out of that list.


def max10(b):
    if b == '0':
        print('ten')
    elif b == '1':
        print('eleven')
    elif b == '2':
        print('twelve')
    elif b == '3':
        print('thirteen')
    elif b == '4':
        print('fourteen')
    elif b == '5':
        print('fifteen')
    elif b == '6':
        print('sixteen')
    elif b == '7':
        print('seventeen')
    elif b == '8':
        print('eighteen')
    elif b == '9':
        print('nineteen')



def word_one(a, b):
    if a == '0':
        word_two(b)
        return
    elif a == '1':
        max10(b)
        return
    elif a == '2':
        print('twenty')
    elif a == '3':
        print('thirty')
    elif a == '4':
        print('forty')
    elif a == '5':
        print('fifty')
    elif a == '6':
        print('sixty')
    elif a == '7':
        print('seventy')
    elif a == '8':
        print('eighty')
    elif a == '9':
        print('ninety')
    else:
        return
    word_two(b)

def word_two(b):
    if b == '0':
        pass
    elif b == '1':
        print('- one')
    elif b == '2':
        print('- two')
    elif b == '3':
        print('- three')
    elif b == '4':
        print('- four')
    elif b == '5':
        print('- five')
    elif b == '6':
        print('- six')
    elif b == '7':
        print('- seven')
    elif b == '8':
        print('- eight')
    elif b == '9':
        print('- nine')

translate = input('What number between 0-99 do you want translated into its English representation? ')
number = []
for num in translate:
    number.append(num)

## if number is less than 10 only run word two
## if number is less than 20 only run max10
## else number is greater than 20, run one then run word one, then word two

word_one(number[0], number[1])



#tens_digit = value//10
#ones_digit = value%10





#def match(set1, set2):
#    if elem in set1 == 1:

