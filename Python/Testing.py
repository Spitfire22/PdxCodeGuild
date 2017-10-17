'''


This is a file I use to text out ideas to see if they will work.


'''


f = open('hammer.txt', 'r')
# g = open('hammer2.txt', 'w')

contents = f.read().lower()
for char in ";,(){}.:[]'\"#+=*&^%$@!\n/-_><0123456789":
    contents = contents.replace(char, "")
word_list = contents.split(" ")
print(word_list)



# g.write(contents)

f.close()
# g.close()



# with open('hammer.txt', 'r') as repub:
#     contents = repub.read()
#
# print(contents)