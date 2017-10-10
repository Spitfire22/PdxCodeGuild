'''

Lab 14

Tremors from below.
The sandy ground shakes and liquifies, a toothy worm appears.

'''

######################## problem 1
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


######################## problem 2

#def lower_case(newword):
#    newword = newword.lower()
#    newword = newword.strip()
#    print(newword)

###  use 'return text' instead of print(newword)

#lower_case("SUPER!")
#lower_case("       NANNANANANA BATMAN       ")

######################## problem 3

#def is_even(a):
#    if a % 2 == 0:
#        print(True)
#    else:
#        print(False)
### def is_even(a):
### #return a%2 == 0
### ## alt -> return a/2 == a//2

### def is_odd(a):
### #return a%2 == 1
### ## alt -> return a%2 == 1

#
#is_even(5)
#is_even(6)

######################## problem 4

#import random

#def random_element(a):
#    print(random.choice(a))

#fruits = ['apples', 'bananas', 'pears', 'tomato', 'avocado', 'peach', 'cherries', 'boysenberry' ]
#random_element(fruits)


### def random_element(a):
###     index = random.randint(0, len(a)-1)
###     return a [index]

######################## Problem 5

#def maximum_of_three(a, b, c):
#    print(max(a, b, c))

### !!! make this : a > b, a > c


#maximum_of_three(2764, 3729, 2738)
#maximum_of_three(-1324, -1326, -1309)

######################## problem 6

#def power(a, b):
#    for i in range(0, b):
#        print(a**i)

#power(2, 20)
#power(4, 11)

######################## problem 7

#def minimum(nums):
#    print('minimum: ', min(nums))

### def minimum(nums):
###     min_value = 100000
###     for num in nums:
###         if num < min_value:
###             min_value = num
###     return min_value

#def maximum(nums):
#    print('maximum: ', max(nums))

#def mean(nums):
#    print('mean: ', sum(nums)/len(nums))

# --- Couldn't get this to work #from statistics import mode

#def mode(nums):
#    print('mode: ', mode(nums))

# --- #

#nums = ([1, 9, 3, 7, 14, 7, 3, 6, 18])
#minimum(nums)
#maximum(nums)
#mean(nums)
# --- # mode(nums)

######################## problem 8

#def reverse_list(nums):
#    print(nums, 'reverse: ', nums[::-1])

#nums = ([1, 9, 3, 7, 14, 7, 3, 6, 18])
#reverse_list(nums)


######################## problem 9

#def common_elements(num1, num2):
#    result = []
#    for element in num1:
#        if element in num2:
#            result.append(element)
#    return print(result)


#yahtzee = ([5, 3, 9, 10, 33, 86, 22, 73, 51, 90, 77, 34, 87, 11])
#monopoly = ([86, 0, 4, 17, 73, 10, 44, 22, 11, 34, 88, 97, 60, 14])
#common_elements(yahtzee, monopoly)

######################## problem 10

#def extract_less_than_ten(nums):
#    result = []
#    for element in nums:
#        if element < 10:
#            result.append(element)
#    return print(result)

#yahtzee = ([5, 3, 9, 10, 33, 86, 22, 73, 51, 90, 77, 4, 87, 11])
#extract_less_than_ten(yahtzee)

######################## problem 11

def combine(nums1, nums2):
    result = []
    result = print(nums1 + nums2)

letters = [1, 2, 3]
numbers = (['a', 'b', 'c'])
combine(letters, numbers)
