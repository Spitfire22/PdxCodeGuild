'''

Computing automated readability index from a file.

4.71(characters/words) + .5(words/sentences) - 21.43 = ARI


'''
text = 'TheRepublic.txt'
republic = open(text, 'r')
contents = republic.read()
contents = contents.replace('\n', '')
for char in '?!':
    contents = contents.replace(char, '.')
sentence_list = contents.split('.')
word_list = contents.split(' ')

# trying to create a condition where it splits all letters from words to create a count.
count = 0
for char in 'abcdefghijklmnopqrstuvwxuyz':
    count += contents.count(char)



print('Number of Sentences: ',len(sentence_list))
sentences = int(len(sentence_list))
words = int(len(word_list))
print('Number of Words: ',len(word_list))
print('Number of Characters: ',count)
#print(len(letter_list)

total = 4.71 * (count/words) + 0.5 * (words/sentences) - 21.43
print_total = (int(total))

ari_scale = {
    1: {'ages': '5-6', 'grade_level': 'Kindergarten'},
    2: {'ages': '6-7', 'grade_level': '1st Grade'},
    3: {'ages': '7-8', 'grade_level': '2nd Grade'},
    4: {'ages': '8-9', 'grade_level': '3rd Grade'},
    5: {'ages': '9-10', 'grade_level': '4th Grade'},
    6: {'ages': '10-11', 'grade_level': '5th Grade'},
    7: {'ages': '11-12', 'grade_level': '6th Grade'},
    8: {'ages': '12-13', 'grade_level': '7th Grade'},
    9: {'ages': '13-14', 'grade_level': '8th Grade'},
    10: {'ages': '14-15', 'grade_level': '9th Grade'},
    11: {'ages': '15-16', 'grade_level': '10th Grade'},
    12: {'ages': '16-17', 'grade_level': '11th Grade'},
    13: {'ages': '17-18', 'grade_level': '12th Grade'},
    14: {'ages': '18-22', 'grade_level': 'College'}
}


grade_level = (ari_scale[print_total]['grade_level'])
age_level = (ari_scale[print_total]['ages'])

print('-'*60)
print('The ARI for', text, 'is', print_total)
print('This corresponds to a', grade_level, 'level of difficulty')
print('that is suitable for an average person', age_level, 'years old.')
print('-'*60)


republic.close()