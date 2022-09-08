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

def hold(): #performs the hold function for the dealer
    if(gameExited == False):
        global numOfGames
        global dealerHand
        dealerHand = rng.next_int(11) + 16
        print(f"\nDealer's hand: {dealerHand}\nYour hand is: {hand}\n ")
        checkWin("Hold")
        numOfGames = numOfGames + 1

def statistics(): #prints the statsistics for the user
    if(gameExited == False):
        percentageOfPlayerWins = round((100*(playerWins / (numOfGames-1))), 1)
        print(f"Number of Player wins: {playerWins}\nNumber of Dealer wins: {dealerWins}\nNumber of tie games: {ties}\nTotal # of games played is: {numOfGames - 1}\nPercentage of Player wins: {percentageOfPlayerWins}%\n ")
        printMenu()

def dealCard(): #deals a card from the dealer
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

def startGame(): #runs the begining of the game
    if(gameExited == False):
        global hand
        global dealerHand
        hand = 0
        dealerHand = 0
        print(f"START GAME #{numOfGames}")
        dealCard()

def checkMenuSelection(): #checks what choice on the menu the user chose
    global gameExited 
    if(menuChoice == "1"):
        dealCard()
    elif(menuChoice == "2"):
        hold()
    elif(menuChoice == "3"):
        statistics()
    elif(menuChoice == "4"):
        gameExited = True
    else:
        print(f"Invalid input!\nPlease enter an integer value between 1 and 4.\n ")
        printMenu()

def printMenu(): #prints out the menu options to the user
    if(gameExited == False):
        global menuChoice
        print("1. Get another card\n2. Hold hand\n3. Print statistics\n4. Exit\n ")
        menuChoice = input("Choose an option: ")
        checkMenuSelection()
        if(gameExited == True):
            exit()

def checkWin(type): #checks whether or not the dealer or user won
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


def main(): #Starts the main function with a loop to easily repeat and exit the game
    while gameExited == False:
        startGame()

main()