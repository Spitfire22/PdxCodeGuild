'''

Lab 14

Tremors from below.
The sandy ground shakes and liquifies, a toothy worm appears.

'''

##### problem 1
#

#def count_letter(letter, word):
#    count = 0
#    for character in word:
#        if character == letter:
#            count = count + 1
#    print(count)

#count_letter('i', 'Antidisestablishmentterianism')

#count_letter('o', 'Pneumonoultramicroscopicsiliconvolcanoconisosis')

## In the above def, for the character in the word, and the letter equals the character,
## increase the count.


## problem 2

#def lower_case(newword):
#    newword = newword.lower()
#    newword = newword.strip()
#    print(newword)

#lower_case("SUPER!")
#lower_case("       NANNANANANA BATMAN       ")

## problem 3

def is_even(a):
    if a % 2 == 0:
        return True
    else:
        False

is_even(5)
is_even(6)