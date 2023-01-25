from src.gensecret import GenSecret
from src.exit import Exit
from src.notfound import NotFound
from src.phonebook import PhoneBook

class Main:
    def __init__(self):
        print("""
* Welcome back 
* App menu
* press 1. to Generate Passwaord
* press 2. to open Phonebook
* press 3. for Exit
        """)
        option = int(input("Chosse an option: "))
        if option == 1 : 
            GenSecret()
            Main()
        elif option == 2:
            PhoneBook()
            Main()
        elif option == 3:
            Exit()
        else:
            NotFound()
            Main()

Main()