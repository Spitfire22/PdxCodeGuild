'''

Lab 23 - Blackjack, are we counting cards? eh! eh! BUSTED.
         Nah, we just givin' n00bs advice.

'''
print(' '*8,'$'*25,'\n')
print('Blackjack Helper - Advice on hands of Blackjack\n')
print(' '*8,'$'*25,'\n')

# Sum the value of all cards, if 'A' present, 'A' = 1
def cardvalue(card):
    if card == 'A':
        return 1
    elif card == 'J' or card == 'Q'or card == 'K':
        return 10
    return int(card)


# This is the total of the cards above.
def total():
    card1 = input('What is your first card? ')
    # cardvalue(card1)
    card2 = input('What is your second card? ')
    # cardvalue(card2)
    card3 = input('What is your third card? ')
    # cardvalue(card3)
    value = cardvalue(card1) + cardvalue(card2) + cardvalue(card3)
##      This is if the total is less than 10 and there is an Ace in the 3 cards... but I cannot get work.
#    if value <= 10:
#        if card1 == 1 or card2 == 1 or card3 == 1:
#            return value + 10
    if value < 17:
        return print("You should hit!")
    if value > 17 and value <= 20:
        return print("In this situation you should stay.")
    if value == 21:
        return print("BooYeah! Blackjack!")
    else:
        return print("Bust, Busted, Game over man!")


total()


