import p1_random as p1 # import the module (do this on the first line of code)
rng = p1.P1Random() # create a P1Random variable (do this in main)

numOfGames = 1
cardValue = 0
cardName = " "
menuChoice = "start"
hand = 0
dealerHand = 0
dealerWins = 0
playerWins = 0
ties = 0
gameExited = False

def option2():
    global numOfGames
    global playerWins
    global dealerWins
    dealerHand = rng.next_int(11) + 16
    print(f"\nDealer's hand: {dealerHand}\nYour hand is: {hand}\n ")

    checkWin(False, True)

    numOfGames = numOfGames + 1
    startGame()

def option3():
    percentageOfPlayerWins = round((100*(playerWins / (numOfGames-1))), 1)
    print(f"Number of Player wins: {playerWins}\nNumber of Dealer wins: {dealerWins}\nNumber of tie games: {ties}\nTotal # of games played is: {numOfGames - 1}\nPercentage of Player wins: {percentageOfPlayerWins}%\n ")
    printMenu()

def checkWin(deal, hold):
    global playerWins
    global dealerWins
    global numOfGames

    if(hold):
        if(hand == 21):
            print(f"\nYour card is a {cardName}!\nYour hand is: {hand}\n ")
            print("\nBLACKJACK! You win!\n ")
            playerWins = playerWins + 1
            numOfGames = numOfGames + 1
            startGame()
        elif(dealerHand > 21):
            print("Dealer exceeded 21! You win!\n ")
            playerWins = playerWins + 1
            numOfGames = numOfGames + 1
            startGame()
        elif(hand > 21):
            print(f"\nYour card is a {cardName}!\nYour hand is: {hand}\n\nYou exceeded 21! You lose.\n")
            dealerWins = dealerWins + 1
            numOfGames = numOfGames + 1
            startGame()
        else:
            print(f"\nYour card is a {cardName}!\nYour hand is: {hand}\n ")
            printMenu()
        if(dealerHand > 21):
            print("You win!")
            playerWins = playerWins + 1
            numOfGames = numOfGames + 1
            startGame()
        elif(hand > 21):
            print(f"\nYour card is a {cardName}!\nYour hand is: {hand}\n\nYou exceeded 21! You lose.\n ")
            dealerWins = dealerWins + 1
            numOfGames = numOfGames + 1
            startGame()
    if(deal):
        if(hand > dealerHand):
            print("\nYou win!\n ")
            playerWins = playerWins + 1
        elif(hand < dealerHand):
            print("\nDealer wins!\n ")
            dealerWins = dealerWins + 1
        elif(hand == dealerHand):
            print("\nIt's a tie! No one wins!\n ")
            ties = ties + 1

def dealCard():
    global gameExited
    if(gameExited == False):
        global cardValue
        global cardName
        global hand
        
        cardValue = rng.next_int(13) + 1
        if(cardValue == 1):
            cardName = "ACE"
        elif(cardValue >= 2 and cardValue <= 10):
            cardName = str(cardValue)
        elif(cardValue == 11):
            cardName = "JACK"
            cardValue = 10
        elif(cardValue == 12):
            cardName = "QUEEN"
            cardValue = 10
        elif(cardValue == 13):
            cardName = "KING"
            cardValue = 10
        hand = cardValue + hand

        checkWin(True, False)
  
def startGame():
    global gameExited
    if(gameExited == False):
        global hand
        global dealerHand
        hand = 0
        dealerHand = 0
        print(f"START GAME #{numOfGames}")
        dealCard()

def checkMenuSelection():
    global gameExited
    if(gameExited == False):
        global dealerHand
        global numOfGames
        global hand
        global dealerWins
        global playerWins
        global ties

        if(menuChoice == "1"):
            dealCard()
        elif(menuChoice == "2"):
            option2()
        elif(menuChoice == "3"):
            option3()
        elif(menuChoice == "4"):
            gameExited = True
        else:
            print(f"Invalid input!\nPlease enter an integer value between 1 and 4.\n ")
            printMenu()
    else:
        print(" ")

def printMenu():
    global gameExited
    if(gameExited == False):
        print("1. Get another card\n2. Hold hand\n3. Print statistics\n4. Exit\n ")
        global menuChoice
        menuChoice = input("Choose an option: ")
        menuChoice = menuChoice.lower()
        checkMenuSelection()

def main():
    while gameExited == False:
        startGame()

main()