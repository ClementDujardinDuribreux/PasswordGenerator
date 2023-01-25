import random

class Password:

    number = '0123456789'
    maj = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    mini = 'abcdefghijklmnopqrstuvwxyz'
    special = '!%#@?/-_|$£*'


    def __init__(self, name, number, maj, mini, special) -> None:
        self.name = name
        self.number = number
        self.maj = maj
        self.mini = mini
        self.special = special
        Password.setPassword(self)

    ## -------------------- ##

    def setPassword(self):
        password = ''
        while len(password) != self.number + self.maj + self.mini + self.special:
            rand = random.randint(1, 4)
            if rand == 1:
                if Password.countNumber(password) != self.number:
                    randomCaractere = random.randint(0,9)
                    password += Password.number[randomCaractere]
            
            elif rand == 2:
                if Password.countMaj(password) != self.maj:
                    randomCaractere = random.randint(0,25)
                    password += Password.maj[randomCaractere]
            
            elif rand == 3:
                if Password.countMin(password) != self.mini:
                    randomCaractere = random.randint(0,25)
                    password += Password.mini[randomCaractere]
            
            elif rand == 4:
                if Password.countSpecial(password) != self.special:
                    randomCaractere = random.randint(0,11)
                    password += Password.special[randomCaractere]

        self.password = password

    ## -------------------- ##

    def countNumber(password:str):
        number = 0
        for carac in password:
            if carac in Password.number:
                number += 1
        return number
    countNumber = staticmethod(countNumber)

    ## -------------------- ##

    def countMaj(password:str):
        maj = 0
        for carac in password:
            if carac in Password.maj:
                maj += 1
        return maj
    countMaj = staticmethod(countMaj)

    ## -------------------- ##

    def countMin(password:str):
        mini = 0
        for carac in password:
            if carac in Password.mini:
                mini += 1
        return mini
    countMin = staticmethod(countMin)

    ## -------------------- ##

    def countSpecial(password:str):
        special = 0
        for carac in password:
            if carac in Password.special:
                special += 1
        return special
    countSpecial = staticmethod(countSpecial)


