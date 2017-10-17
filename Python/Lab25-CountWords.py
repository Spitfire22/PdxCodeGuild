'''

Go find a book in project Gutenberg, download it in UTF-8 file and get a word count on specific
words within the book.


'''

# with open('TheRepublic.txt', 'r') as repub:
#     contents = repub.read()


repub = open('TheRepublic.txt', 'r')
contents = repub.read().lower()
for char in "\n.?!:;,(){}[]'\"#+=*&^%$@/-_><0123456789":
    contents = contents.replace(char, ' ')
word_list = contents.split(' ')
#print(word_list)

# keys  = word, when word not found, add. if found add to value.
# sorted(_*dictionaryname*_.items())
#
#
word_count = {}

for i in range(len(word_list)-1):
    if word_list[i] == '' or word_list[i+1] == '':
        continue
    pair = word_list[i]+' '+word_list[i + 1]
    if pair not in word_count:
        word_count[pair] = 1
    else:
        word_count[pair] += 1

# for word in word_list:
#     # if word != '':
#     #     pass
#     if word not in word_count:
#         word_count[word] = 1
#     else:
#         word_count[word] += 1
#print(word_list)

# print(word_count)

words = list(word_count.items()) # list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(40, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])




#
# def lower_case(text):
#     text = text.lower()
#     text = text.strip()
#     text = text.replace('.','').replace(',','').replace(':','').replace('?','').replace('!','')
#
# lower_case(contents)



#words =