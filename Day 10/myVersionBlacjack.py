import random
import os
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
playGame = "y"
GameOver = False
getAnotherCard = "n"
PlayerCards = []
ComputerCards = []
CardsList = []

def defHit():
    return random.choice(cards)

def defCardsSum(cardsList):
    while sum(cardsList) > 21 and 11 in cardsList:
        cardsList[cardsList.index(11)] = 1
    return sum(cardsList)

def defPrintPlayerCards():
    print(f"Your cards: {PlayerCards}, current score: {sum(PlayerCards)}")
    print(f"Computer's first card: {ComputerCards[0]}")

def defGameOver(winner, blackjack):
    print(f"Your final hand: {PlayerCards}, final score: {sum(PlayerCards)}")
    print(f"Computer's final hand: {ComputerCards}, final score: {sum(ComputerCards)}")
    if blackjack:
        print(f"{winner} has a Blackjack!")
    elif winner == "Computer" and sum(PlayerCards) > 21:
        print("You went over. You lose")
    elif winner == "Player" and sum(ComputerCards) > 21:
        print("Computer went over. You win")
    else:
        print(f"The winner is {winner}")

def defGameOverCalculate():
    print(f"Your final hand: {PlayerCards}, final score: {sum(PlayerCards)}")
    print(f"Computer's final hand: {ComputerCards}, final score: {sum(ComputerCards)}")
    if sum(ComputerCards) > sum(PlayerCards):
        print("You lose")
    elif sum(ComputerCards) < sum(PlayerCards):
        print("You win")
    else:
        print("DRAW")

while playGame == "y":
    print(logo)
    playGame = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if playGame == "y":
        os.system('cls')
        print(logo)
        GameOver = False
        PlayerCards = []
        ComputerCards = []
        CardsList = []
        getAnotherCard = "n"

    for i in range(2):
        PlayerCards.append(defHit())
        ComputerCards.append(defHit())

    while not GameOver:
        PlayerCardsScore = defCardsSum(PlayerCards)
        ComputerCardsScore = defCardsSum(ComputerCards)
        defPrintPlayerCards()

        if sum(ComputerCards) == 21:
            defGameOver("Computer", True)
            GameOver = True
        elif sum(PlayerCards) == 21:
            defGameOver("Player", True)
            GameOver = True
        elif sum(ComputerCards) > 21:
            defGameOver("Player", False)
            GameOver = True
        elif sum(PlayerCards) > 21:
            defGameOver("Computer", False)
            GameOver = True
        else:
            getAnotherCard = input("Type 'y' to get another card, type 'n' to pass: ")
            while getAnotherCard == "y" and PlayerCardsScore < 21:
                PlayerCards.append(defHit())
                PlayerCardsScore = defCardsSum(PlayerCards)
                defPrintPlayerCards()
                if PlayerCardsScore < 21:
                    getAnotherCard = input("Type 'y' to get another card, type 'n' to pass: ")

            while ComputerCardsScore < 17 and PlayerCardsScore < 22:
                ComputerCards.append((defHit()))
                ComputerCardsScore = defCardsSum(ComputerCards)
                if ComputerCardsScore > 21:
                    defGameOver("Player", False)
                    GameOver = True
            if ComputerCardsScore < 21 and PlayerCardsScore < 21:
                defGameOverCalculate()
                GameOver = True
else:
    print("Good Game!!!")
