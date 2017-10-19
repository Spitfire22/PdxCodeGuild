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
    print('\nCreating a new user - Please answer the following questions\n')
    name_input = input('What is your name? \n\t')
    fav_color = input('What is your favorite color? \n\t')
    fav_fruit = input('What is your favorite fruit? \n\t')
    new_contact = {'name': name_input, 'favorite color': fav_color, 'favorite fruit': fav_fruit}
    new = contacts.append(new_contact)
    #retrieve = [name for name in contacts if name['name'] == name_input]
    print('\nYou have added: ', new_contact)

def print_names():
    name = [name['name'] for name in contacts]
    print(sorted(name))

def retrieve_user():
    print('\nRetrieving a users information - Here are your users: ')
    print_names()
    prompt = input('\nWhich user do you want to view? \n\t')
    contact = find_user(prompt)
    retrieve = [name for name in contacts if name['name'] == prompt]
    if contact is None:
        print(prompt, 'is a contact not found in the database, check or update the spelling or create a new contact')
        return
    print(retrieve)
    # retrieve = [name for name in contacts if name ['name']==prompt]
    # print(retrieve)
    while True:
        command = input('\nDo you want to view another user? Yes / No? \n\t').lower()
        if command in ['no', 'n', 'nah', 'naw']:
            return
        elif command in ['yes', 'y', 'yeah', 'yea', 'yeah dude']:
            retrieve_user()
        else:
            pass


def find_user(name):
    for contact in contacts:
        if contact['name'] == name:
            return contact
    return None

def update_user():
    print('Updating users menu... 3... 2... 1... Loaded!\n')
    print_names()
    prompt = input('\nWhich user do you want to edit? \n\t')
    #e = [name for name in contacts if name['name'] == prompt][0]
    contact = find_user(prompt)
    retrieve = [name for name in contacts if name['name'] == prompt]
    if contact is None:
        print(prompt, 'is a contact not found in the database, check or update the spelling or create a new contact')
        return
    print(retrieve)
    while True:
        command_update = input('\nWhat do you want to edit? \nName, Color, or Fruit? Or you can type \'exit\' or \'done\' to return to main menu. \n').lower()
        if command_update in ['done', 'quit', 'exit']:
            return
        elif command_update in ['name', 'names']:
            name_input = input('\nYou want to change the name to? \n\t')
            # print(name_input)
            contact['name'] = name_input
            print('\nYou have changed their name: ', contact,'\n')
        elif command_update in ['color', 'colour']:
            color_input = input('\nWhat is their new favorite colour? \n\t')
            contact['favorite color'] = color_input
            print('\nColor has been changed: ', contact,'\n')
        elif command_update in ['fruit', 'fruity']:
            fruit_input = input('\nTastebuds change, what is their new favorite fruit? \n\t')
            contact['favorite fruit'] = fruit_input
            print('\nNew tasty changes!', contact,'\n')
        else:
            break

def delete_user():
    print('\nDeleting a user from the list\n')
    print_names()
    prompt = input('\nWhich user in the list do you want to delete? \n\t')
    contact = find_user(prompt)
    # retrieve = [name for name in contacts if name['name'] == prompt]
    if contact is None:
        print(prompt, 'is a contact not found in the database, check or update the spelling or create a new contact')
        return
    # print(retrieve)
    confirmation = input('Are you sure? Yes or No\n\t').lower()
    if confirmation in ['no', 'n']:
        return
        #delete the user use .pop
    elif confirmation in ['yes', 'y']:
        contacts.remove(contact)
        print(prompt, 'was removed!')


def ask():
    while True:
        command = input('\n|Contact List| Type a Command: Create, Retrieve, Update, Delete, or Exit ?\n\t').lower()
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


### Version 3 ---------------------------------------
### On exit - place 'the_keys' back at the beginning
### join the keys with ','
### and join the strings with a new line.
### Load back into the file.

#I need to remove the keys from the contacts list before splitting by ',' and new line



# use contacts
new_contact = ""
for i in contacts:
    new_contact += str(i) + ',\n'
print(contacts)
print(new_contact)



#
# with open('contacts_2.csv', 'w') as file1:
#     file1.write('\n'.join(contacts))
# print(contacts)


#
# contacts.update({'name': name, 'favorite color': fav_color, 'favorite fruit': fav_fruit})
#
# print(contacts)


# I was thinking about making more functions to include a possible option
# while in the retrieve function to switch to update user.
# def update_prompt():
#     print('\nUpdating a users information - What user do you want to update?')
#     only_names()
#     input('Which user do you want to edit? ')
#     pass


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
