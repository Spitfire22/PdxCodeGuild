'''


Creating a contact list using a comma seperated value (CSV) file.



'''
with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    #print(lines)

## take the contacts.csv file and create a for loop that makes each line
## into a seperate dictionary and use the first line of the file to determine the keys.
## The values following are in order to the keys.

the_keys = lines.pop(0).split(',')
#print(the_keys)
contacts = []

for line in lines:
    contact = {}
    line = line.split(',')
    for i in range(len(line)):
        contact[the_keys[i]] = line[i]
    contacts.append(contact)

#print(contacts)

## Version 2 ----------------------------------
## Implement CRUD
## Create a record - ask a new contact and for each attribute

def create_user():
    print('Creating a new user - Please answer the following questions')
    name = input('What is your name? ')
    fav_color = input('What is your favorite color? ')
    fav_fruit = input('What is your favorite fruit? ')
    new = contacts.append({'name': name, 'favorite color': fav_color, 'favorite fruit': fav_fruit})

def only_names():
    name = [name['name'] for name in contacts]
    print(name)
    #format this list into a string and order it alphabetically, then print it


def retrieve_user():
    print('Retrieving a users information - What user do you want to view?')
    only_names()
    input('Which user do you want to edit? ')
    pass

def update_user():
    print('Updating a users information - What user do you want to update?')
    # we will need the list of names again here to select.

def delete_user():
    print('Deleting a user from the list - which user do you want to delete?')
    #selecting a user to delete
    while True:
        confirmation = input('Are you sure? Yes or No')
        if confirmation in ['yes', 'Yes', 'YES', 'y']:
            pass
            #delete the user use .pop
        else:
             return


def ask():
    while True:
        command = input('|Contact List| Type a Command: Create, Retrieve, Update, Delete, or Exit ?').lower()
        if command in ['done', 'quit', 'exit']:
            break
        elif command == 'retrieve':
            retrieve_user()
        elif command == 'create':
            create_user()
        elif command == 'update':
            update_user()
        elif command == 'delete':
            delete_user()
        else:
            ask()

ask()
print(contacts)


#
# contacts.update({'name': name, 'favorite color': fav_color, 'favorite fruit': fav_fruit})
#
# print(contacts)












#contacts = {
# 1: {values in keys1: values in lines1}
# 2: {values in keys2: values in lines2}
# 3: {values in keys3: values in lines3}
# }
#
# split the keys into 3, split and apply the values in same order
#


# for word in key:
#     pass


### NNNOOOOPPPEEEE:
# 1 print(the_keys.split(' '))
# 2 keys = tuple(the_keys)
# print(keys)
# 3 for char in ',':
#     the_keys = the_keys.replace(char, ', ')
# print(the_keys)
