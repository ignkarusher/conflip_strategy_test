import math
import random

def coinfliper(money, total_flips, face_chosen, starting_bet):
    bet = starting_bet
    round = 1
    for i in range(total_flips):
        coin = (random.randint(1, 2))
        if coin == 1:
            coin = "HEADS"
            print("HEADS")
        else:
            coin = "TAILS"
            print("TAILS")
        if coin == face_chosen:
            money += bet
            bet = starting_bet
        else:
            money -= bet
            bet = bet*2
        if money <= 0:
            print("You are broke! This was flip #{}".format(str(i+1+(round-1)*total_flips)))
            exit(0)
        print(money)
    print("Repeat process with current money? Y/N")
    continueflipping = input().upper()
    if continueflipping == "Y":
        coinfliper(money, total_flips, face_chosen, starting_bet)
        round += 1
def setup():
    print("Starting Money: ($)")
    try:
        money = int(input())
    except:
        print("Number has to be an integer. Program terminated.")
        exit(-1)

    print("Total amount of flips:")
    try:
        total_flips = int(input())
    except:
        print("Number has to be an integer. Program terminated.")
        exit(-1)

    print("Face chosen to rule the bets:")
    face_chosen = input().upper()
    if face_chosen != "HEADS" and face_chosen != "TAILS":
        print("Face chosen has to be \"Heads\" or \"Tails\"")
        exit(-1)

    print("Starting bet: ($)")
    try:
        starting_bet = int(input())
    except:
        print("Number has to be an integer. Program terminated.")
        exit(-1)



    coinfliper(money, total_flips, face_chosen, starting_bet)

setup()
