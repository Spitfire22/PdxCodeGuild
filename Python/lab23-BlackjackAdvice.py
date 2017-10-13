'''

Lab 23 - Blackjack, are we counting cards? eh! eh! BUSTED.
         Nah, we just givin' n00bs advice.

'''
print(' '*8,'$'*25,'\n')
print('Blackjack Helper - Advice on hands of Blackjack\n')
print(' '*8,'$'*25,'\n')

# Sum the value of all cards, if 'A' present, 'A' = 1
def cardvalue(c1, c2, c3):
    pass

# If 'A' in list and =< 10, A = 11
def aces():
    pass

# This is the total of the cards above.
def total():
    pass

# total > 17 'Hit, total >= 17 and total < 21  'Advise to stay', total == 21 'Blackjack!', total < 21 'Busted'
def advice():
    pass

card1 = input('What is your first card? ')
#cardvalue(card1)
card2 = input('What is your second card? ')
#cardvalue(card2)
card3 = input('What is your third card? ')
#cardvalue(card3)
selectcards = str([card1, card2, card3])

cards = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}