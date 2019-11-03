import random
import sys
import time


class User:
    def __init__(self, n, a, r):
        self.name = n
        self.age = a
        if r == "W":
            self.race = "White"
        elif r == "B":
            self.race = "Black"
        elif r == "A":
            self.race = "Asian"
        else:
            self.race = "Fukface"
        self.money = 100

    def add_money(self, var):
        self.money += var

    def sub_money(self, var):
        self.money -= var

    def user_name(self, str):
        self.name = str


def create_user():
    n = input("Hello, welcome to fucktown, What is your name? ")
    a = input("What is your age? ")
    r = input("What is your race? (W)hite,(B)lack, or (A)sian? ")
    user = User(n, a, r)
    print(user.name, user.age, user.race)
    return user


def define_starting_money(user):
    edu = input("Do you have a (H)S Diploma, (A)ssociate's degree, (B)achelor's degree,(M)aster's degree, or (P)HD? ")
    if edu == "H":
        user.education = "High school diploma"
        user.money = 50
    elif edu == "A":
        user.education = "Associate's degree"
        user.money = 100
    elif edu == "B":
        user.education = "Bachelor's degree"
        user.money = 10
    elif edu == "M":
        user.education = "Master's degree"
        user.money = 5
    elif edu == "P":
        user.education = "PHD"
        user.money = 100
    else:
        user.education = "Stupid-ass thot"
        user.money = 1

    return user


def create_password_for_user(user):
    pw = input("Please input a password, you will need this later on:  ")
    user.password = pw
    return user


def rock_paper_scissors(user):
    print("Welcome to rock, paper, scissors!")
    bet = input("How much would you like to bet?")
    try:
        bet = int(bet)
    except:
        "Hey, put in a fucking number this time shithead, or the program will crash"
        bet = int(input("How much would you like to bet?  "))
    if bet > user.money:
        print("Hey fuckface, thats more money than you have, the bet is now just your entire balance")
        bet = user.money
    f = input('(r)ock, (p)aper, or (s)cissors? ')
    num = random.randint(1, 3)
    if f == "r":
        a = 1
    elif f == 'p':
        a = 2
    else:
        a = 3
    if a == 1 and num == 1:
        x = "Draw"
        print("Rock bashes Rock")
    elif a == 1 and num == 2:
        x = "Computer wins!"
        print("Paper covers rock!")
    elif a == 1 and num == 3:
        x = "You win!"
        print("Rock beats scissors!")
    elif a == 2 and num == 1:
        x = "You win!"
        print("Paper covers rock!")
    elif a == 2 and num == 2:
        x = "Draw"
        print("Paper scissors paper")
    elif a == 2 and num == 3:
        x = "Computer wins!"
        print("Scissors cuts paper!")
    elif a == 3 and num == 1:
        x = "Computer wins!"
        print("Rock crushes scissors!")
    elif a == 3 and num == 2:
        x = "You win!"
        print("Scissors cuts paper!")
    elif a == 3 and num == 3:
        x = "Draw"
        print("Scissors scissor each other")
    else:
        print("Youre a fucking retard, next time type in the right fucking letter. ")
        print(num)
        user.sub_money(10)
        print("I took $10 because you're a fucking retard, I would'dve expected better from someone with a",
              user.education)
        print("Your balance is now ", user.money)
        x = "Computer wins"
    if x[0] == "D":
        print("It is a draw! No money will be taken!")
    if x[0] == "Y":
        print("You win! Your bet will be doubled back to you!")
        user.add_money(bet)
    if x[0] == "C":
        print("You lose! Your bet will be deducted from you!")
        user.sub_money(bet)
    print("Thanks for playing!")
    time.sleep(.2)
    return user

def main():
    if Main_user.money <= 0:
        print("hey fuckface, youre broke!!! Time to go bankrupt!")
        Main_user.bankrupt_count += 1
        if Main_user.bankrupt_count > 5:
            print("Hey, you have gone bankrupt like way too much, you are getting kicked off the planet, have fun in hell!")
            time.sleep(5)
            sys.exit()
        else:
            bankruptcy(Main_user)
    choice = input("Would you like to play (r)ock paper scissors, (v)iew balance, go to (c)ollege, or e(x)it? ")
    if choice == "r":
        rock_paper_scissors(Main_user)
    if choice == 'v':
        print('Your balance is', Main_user.money)
    if choice == 'c':
        college(Main_user)
    if choice == 'x':
        print("Goodbye")
        time.sleep(2)
        sys.exit()
    else:
        "Youre a fucking idiot, try again"
    main()

def bankruptcy(user):
    print("Hey you kinda fucked yourself eh?")
    time.sleep(1)
    print("Well now you're going to have to answer a couple questions correctly in order to get some money back.")
    time.sleep(1)
    if user.bankrupt_count == 1:
        f = input("First thing you need to answer:\nWhat is Netwon's first law of motion?\n(A)An object in motion will remain in motion.\n(B) "
              "The acceleration of an object as produced by a net force is directly proportional to the magnitude of the net force, in the same direction as the net force, "
              "and inversely proportional to the mass of the object.\n(C) For every action, there is an equal and opposite reaction.\n")
        if f == "A":
            print("Congrats, youre not a fucktard, here is $10 because I feel bad for you.")
            user.add_money(10)
        else:
            print("You are a fucking bitch, go commit toaster bath. BYE")
            time.sleep(3)
            sys.exit()
    elif user.bankrupt_count == 2:
        f = input("Next one: Who is the best president to ever live? (A)Donald Trump\n(B)Barack Obama\n(C)Richard Nixon")
        if f == "A":
            print("Congrats, you are not a libtard, here's $100")
            user.add_money(100)
        else:
            print("Youre a lib cuck")
            time.sleep(3)
            sys.exit()
    else:
        f = input("QUESTION: What does NNN stand for? (Type it out)")
        f = f.strip()
        f = f.lower()
        if f == "no nut november":
            print("ay, you're not a total bitch, here's $50")
            user.add_money(50)
        else:
            print("wao, youre a cuck")
            time.sleep(2)
            sys.exit()
            
def college(user):
    if user.education == "High school diploma":
        print("It costs $50 to get an associate's degree.")
        if user.money >= 50:
            f = input("Do you want to get your associate's? Y/N ")
            if f == "Y":
                user.sub_money(50)
                user.education = "Associate's degree"
            else:
                print("K BYE BBY")
        else:
            print("You literally broke af, GTFO, also im taking $5")
            user.sub_money(5)


    elif user.education == "Associate's degree":
        print("It costs $50 to get an bachelor's degree.")
        if user.money >= 50:
            f = input("Do you want to get your bachelor's? Y/N ")
            if f == "Y":
                user.sub_money(50)
                user.education = "Bachelor's degree"
            else:
                print("K BYE BBY")
        else:
            print("You literally broke af, GTFO, also im taking $5")
            user.sub_money(5)
    elif user.education == "Bachelor's degree":
        print("It costs $100 to get a Master's degree.")
        if user.money >= 100:
            f = input("Do you want to get your Master's? Y/N ")
            if f == "Y":
                user.sub_money(100)
                user.education = "Master's degree"
            else:
                print("K BYE BBY")
        else:
            print("You literally broke af, GTFO, also im taking $10")
            user.sub_money(10)
    elif user.education == "Master's degree":
        print("It costs $150 to get an PHD.")
        if user.money >= 150:
            f = input("Do you want a PHD? Y/N ")
            if f == "Y":
                user.sub_money(150)
                user.education = "PHD"
            else:
                print("K BYE BBY")
        else:
            print("You litterally broke af, GTFO, also im taking $15")
            user.sub_money(15)

    elif user.education == "PHD":
        print(
            "You already have a PHD, now you are classified as a Stupid-ass thot because you tryin'\n to spend your whole life in college. GTFO")
        user.education = "Stupid-ass thot"

    else:
        print("Hey thot, it costs $10 to get your HS Diploma.")
        if user.money >= 10:
            f = input("Do you want your damn diploma? Y/N ")
            if f == "Y":
                user.sub_money(10)
                user.education = "High school diploma"
            else:
                print("K BYE BBY")
        else:
            print("You litterally broke af, GTFO, also im taking $1")
            user.sub_money(1)


Main_user = create_user()
Main_user.bankrupt_count = 0

define_starting_money(Main_user)
create_password_for_user(Main_user)

main()
