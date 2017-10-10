import random

print('$'*35)
print(' '*3, 'Not for investment purposes', ' '*3)
print('\n Pick 6 Lottery game! See how much you COULD win!\n\n based on a computer simulation...\n')
print('$'*35)

## End game intro


# this 'pick6' is the lottery generated numbers used to compare to the purchased tickets
def pick6():
    digits = []
    for i in range(6):
        lotto = random.randint(1, 99)
        digits.append(lotto)
    #print('These are the winning Lottery numbers:', digits)
    return digits

def match(set1, set2):
   count = 0
   for element in set1:
       if element in set2:
           count += 1
   return count

winning_tickets = pick6()
balance = 0

for game in range(1000):
    bought_ticket = pick6()
    balance -= 2
    matches = match(winning_tickets, bought_ticket)
    if matches == 0:
        pass
    elif matches == 1:
        balance += 2
    elif matches == 2:
        balance += 7
    elif matches == 3:
        balance += 100
    elif matches == 4:
        balance += 50000
    elif matches == 5:
        balance += 1000000
    elif matches == 6:
        balance += 25000000

print('After 1000 tickets at $2 dollars each your balance is:', balance)

ROI = (balance - 2000)/2000

print('\nYour return on \'investment\' is:', ROI, "%" '\nThanks for supporting your local Oregon schools!')




## Calc ROI:  (earnings - expenses)/expenses



#def cash(a, b, c, d, e, f, g):
#    i = 0
#    if a > b and a > c and a > d and a > e and a > f and a > g:
#        i += 0
#    elif b > a and b > c and b > d and b > e and b > f and b > g:
#        i += 2

#def purchase(set1, set2):
    # when a series of numbers matches in the winning ticket give it a value
#    match = []
#    icash = 1
#    for element in set1:
#        if element in set2:
#            icash += 1
#    return print(icash)
