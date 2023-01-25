import json
class PhoneBook:
    def __init__(self):
        newContact = {
            'name' : '',
            'number' : ''
        }
        jsonFile = open('./json/contacts.json')
        contact = json.load(jsonFile)
        print('SAVED CONTACTS')
        for i in contact:
            print('====================')
            print(i['name'])
            print(i['number'])
        print('\nCreate contact')
        newContact['name'] = input('Enter name: ')
        newContact['number'] = input('Enter number: ')
        contact.append(newContact)
        file = open("./json/contacts.json", 'w')
        string = json.dumps(contact)
        file.write(string)
        print(string)
        file.close()
        print('contact saved !')
