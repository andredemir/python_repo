import string
from random import random  # Import random module

number = random() * 100


def zahlenRaten():
    print(int(number))
    inputNumber = int(input("Enter a number: "))
    if int(number) > inputNumber:
        print("The inputNumber is greater than number")
        zahlenRaten()
    elif int(number) == inputNumber:
        print("The inputNumber is equal to number")
    else:
        print("The inputNumber is less than number")
        zahlenRaten()


def wuerfelSpiel():
    wuefel1 = random() * 6
    wuefel2 = random() * 6
    print("Würfel 2: " + int(wuefel2).__str__())
    print("Würfel 1: " + int(wuefel1).__str__())
    if int(wuefel2) + int(wuefel1) == 7:
        print("You win")
    else:
        print("You lose")


def wortZaehler(text):
    print(text.split(" ").__len__())


def temperaturUmrechner(tempinC):
    tempinF = (tempinC * 9 / 5) + 32
    print(tempinF)


# temperaturUmrechner(20)
# wortZaehler("Hallo Welt wie geht es dir?")
# wuerfelSpiel()
# zahlenRaten()
# passwortGenerator()


def galgenmaennchen(wort):
    newwort = []
    for i in range(0, wort.__len__()):
        newwort.append("_")
    if checkCondition(wort, newwort, ""):
        return


def checkCondition(wort, newwort, checkwort):
    checkword = checkwort
    char = input("Enter a char: ")
    if char.__len__() > 1:
        print("Only one char is allowed")
        checkCondition(wort, newwort, checkwort)
    if not exist(char, wort):
        print("The char is not in the word")
        checkCondition(wort, newwort, checkwort)
    else:
        indices = getIndexOfChar(char, wort)
        print("The char is in the word at indices:", indices)
        for index in indices:
            newwort[index] = char
        print(newwort)
        for i in range(0, len(newwort)):
            checkword = checkword + newwort[i]
        if checkword == wort:
            print("You guessed it correclty the word is: " + wort + " you win")
            return True
        else:
            checkCondition(wort, newwort, checkwort)


def exist(char, wort):
    count = wort.count(char)
    if count > 0:
        return True
    else:
        return False


def getIndexOfChar(char, wort):
    indices = []
    for i in range(len(wort)):
        if wort[i] == char:
            indices.append(i)
    return indices


#galgenmaennchen("schmetterling")
