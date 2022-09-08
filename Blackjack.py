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
    if(gameExited == False):
        global numOfGames
        global dealerHand
        dealerHand = rng.next_int(11) + 16
        print(f"\nDealer's hand: {dealerHand}\nYour hand is: {hand}\n ")
        checkWin("Hold")
        numOfGames = numOfGames + 1

def option3():
    if(gameExited == False):
        percentageOfPlayerWins = round((100*(playerWins / (numOfGames-1))), 1)
        print(f"Number of Player wins: {playerWins}\nNumber of Dealer wins: {dealerWins}\nNumber of tie games: {ties}\nTotal # of games played is: {numOfGames - 1}\nPercentage of Player wins: {percentageOfPlayerWins}%\n ")
        printMenu()

def dealCard():
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
        checkWin("Deal")

def startGame():
    if(gameExited == False):
        global hand
        global dealerHand
        hand = 0
        dealerHand = 0
        print(f"START GAME #{numOfGames}")
        dealCard()

def checkMenuSelection():
    global gameExited
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

def printMenu():
    if(gameExited == False):
        global menuChoice
        print("1. Get another card\n2. Hold hand\n3. Print statistics\n4. Exit\n ")
        menuChoice = input("Choose an option: ")
        checkMenuSelection()
        if(gameExited == True):
            exit()

def checkWin(type):
    if(gameExited == False):
        global playerWins
        global dealerWins
        global numOfGames
        global ties
        winnerChosen = False
        if(hand == 21):
            print(f"\nYour card is a {cardName}!\nYour hand is: {hand}\n ")
            print("\nBLACKJACK! You win!\n ")
            winnerChosen = True
            playerWins = playerWins + 1
            numOfGames = numOfGames + 1
            startGame()
        if(dealerHand > 21):
            print("You win!\n ")
            winnerChosen = True
            playerWins = playerWins + 1
            numOfGames = numOfGames + 1
            startGame()
        if(hand > 21):
            print(f"\nYour card is a {cardName}!\nYour hand is: {hand}\n\nYou exceeded 21! You lose.\n")
            winnerChosen = True
            dealerWins = dealerWins + 1
            numOfGames = numOfGames + 1
            startGame()

        if(type == "Hold"):
            if(hand > dealerHand):
                print("\nYou win!\n ")
                winnerChosen = True
                playerWins = playerWins + 1
                numOfGames = numOfGames + 1
                startGame()
            if(hand < dealerHand):
                print("\nDealer wins!\n ")
                winnerChosen = True
                dealerWins = dealerWins + 1
                numOfGames = numOfGames + 1
                startGame()
            if(hand == dealerHand):
                print("\nIt's a tie! No one wins!\n ")
                winnerChosen = True
                ties = ties + 1
                numOfGames = numOfGames + 1
                startGame()

        if(winnerChosen == False):        
            print(f"\nYour card is a {cardName}!\nYour hand is: {hand}\n ")
            printMenu()


def main():
    while gameExited == False:
        startGame()

main()