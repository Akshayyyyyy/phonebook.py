import random

class GenSecret:
    def __init__(self) :
        secret = ''
        pattern = "qwertyuiopasdfghjklzxcvbnm.,/;'[]1234567890-=`1~!@#$%^&*()_+-<>?"
        choise = int(input('Enter lenght: '))
        for i in range(choise):
            limit = len(pattern)-1 
            index = random.randint(0, limit)
            secret += pattern[index]
        print(secret)