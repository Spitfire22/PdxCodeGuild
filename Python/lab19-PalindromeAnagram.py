'''

Lab19 - Palindrome and Anagram checker

'''

## palindrome - if the string is equal to the reverse of the same string return true

# def palindrome(a,b):
#     if a == b:
# ##    if a == (a[::-1]):
#         print('\'', word, '\'', 'is a palindrome')
#         return
#     elif a != b:
# ##    elif a != (a[::-1]):
#         print('\'', word, '\'', 'is not a palindrome')
#         return
#     else:
#         return
#
# word = input('Palindrome checker - Enter a word: ')
# reverse = (word[::-1])
#
# palindrome(word, reverse)


## anagram Checker - input two words and determine if they are an anagram.

def wordfilter(a, b,):
    string1 = a
    string2 = b
    a = a.lower()
    a = a.replace(' ','')
    a = sorted(a)
    a = ''.join(a)
#    print(a)
    b = b.lower()
    b = b.replace(' ', '')
    b = sorted(b)
    b = ''.join(b)
#    print(b)
    if a == b:
        print('\'',string1,'\'','and','\'',string2,'\'','are anagrams')
    elif a != b:
        print('\'',string1,'\'','and','\'',string2,'\'','are not anagrams')



word_one = input('Anagram checker - Enter the first word: ')
word_two = input('Now for the second word: ')


wordfilter(word_one, word_two)