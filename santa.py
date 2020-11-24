import random as r
import pyfiglet, os
import getpass

def printTree():
    print(20*' '+'/\\')
    for i in range(1,20):
        s = ''.join(r.choice(['*','~',r.choice(['¢','•','*','~'])]) for i in range(i*2))
        sl = r.choice(['/','¢'])
        sr = r.choice(['\\','•'])
        print((20-i)*' '+sl+s+sr)

    print((20-1)*' ' + '\'||\'')
    print(' '+20*2*'-')

def printMenu(loggedIn):
    print("\n\n\n       How can I help you?")
    print("         1. Create an account")
    print("         2. Log In")
    if (loggedIn):
        print("         3. Check my gift list")
        print("         4. Log out")

    return input("         ---> ")


def choiceOne():
    userList = next(os.walk('.'))[1]        #Get names of folders (users)

    user = input("\nUsername: ")
    while(user in userList):
        print("Username already exists! Please choose another username.")
        user = input("\nUsername: ")

    pwd = getpass.getpass("\nPassword: ")
    pwd2 = getpass.getpass("Confirm password: ")

    while(pwd != pwd2):
        print("Passwords do not match")
        pwd = getpass.getpass("\nPassword: ")
        pwd2 = getpass.getpass("Confirm password: ")

    os.mkdir(os.getcwd()+ "/" + user)
    toWrite = user + "\t" + pwd
    f = open(os.getcwd()+ "/" + user+"/cred.txt", "x")
    f2 = open(os.getcwd()+ "/" + user+"/list.txt", "x")
    f.write(toWrite)
    f2.write("")

    print("User created successfully!")

    return



def choiceTwo():
    userList = next(os.walk('.'))[1]        #Get names of folders (users)
    tries = 3

    user = input("\nUsername: ")
    while(user not in userList):
        print("Username does not exist!")
        user = input("\nUsername: ")
    

    # get pwd
    f = open(os.getcwd()+ "/" + user+"/cred.txt", "r")
    pwd = f.read().split("\t")[1]

    while(tries != 0):
        pwdAttempt = getpass.getpass("Password: ")
        if (pwd != pwdAttempt):
            print("Wrong password\n")
        else:
            break
        tries -= 1

    print("Logged in successfully")    

    return user


def choiceThree(user):
    f = open(os.getcwd()+ "/" + user+"/list.txt", "r")
    giftList = f.read()

    if (giftList == ""):
        print("GIFT LIST IS EMPTY")
    else:
        print("GIFT LIST: \n")
        print(giftList + "\n")


    
    r = input("Do you want to add to your gift list? [y/n] ")

    while(r != 'y' and r != 'n'):
        r = input("Do you want to add to your gift list? [y/n] ")

    if(r == 'y'):
        f = open(os.getcwd()+ "/" + user+"/list.txt", "a")
        rec = input("Who is receiving the gift? ")
        gift = input("What gift is it? ")
        f.write("\n" + rec +"\t"+gift)

    return



loggedIn = False
account = ""
while(True):
    print(pyfiglet.figlet_format(" Welcome to Santa's PyHelper!"))
    printTree()

    if (loggedIn):
        print(" LOGGED IN AS: " + account + "\n")
        choice = int(printMenu(True))
    else:
        print(" NOT LOGGED IN\n")
        choice = int(printMenu(False))


    if (loggedIn):
        while(choice < 1 or choice > 4):
            print("Please choose an option between 1 and 4")
            choice = int(printMenu(True))

    else:
        while(choice < 1 or choice > 2):
            print("Please choose an option between 1 and 2")
            choice = int(printMenu(False))


    if (choice == 1):
        choiceOne()

    if (choice == 2):
        account = choiceTwo()
        loggedIn = True

    if (choice == 3):
        choiceThree(account)

    if(choice == 4):
        account = ""
        loggedIn = False