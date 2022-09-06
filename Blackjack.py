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

def dealCard(): 
    global cardValue
    global cardName
    global hand
    global dealerWins
    global numOfGames
    global playerWins
    cardValue = rng.next_int(13) + 1
    if(cardValue == 1):
        cardName = "ACE"
    elif(cardValue >= 2 and cardValue <= 10):
        cardName = str(cardValue)
    elif(cardValue == 11):
        cardName = "JACK"
    elif(cardValue == 12):
        cardName = "QUEEN"
    elif(cardValue == 13):
        cardName = "KING"
    
    hand = cardValue + hand
    if(hand == 21):
        print("BLACKJACK! You win!")
        playerWins = playerWins + 1
        numOfGames = numOfGames + 1
        startGame()
    elif(dealerHand > 21):
        print("Dealer exceeded 21! You win!")
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

def printMenu():
    print("1. Get another card\n2. Hold hand\n3. Print statistics\n4. Exit\n ")
    global menuChoice 
    menuChoice = input("Choose an option: ").lower()
    checkMenuSelection()

def startGame():
    global hand
    global dealerHand
    hand = 0
    dealerHand = 0
    print(f"START GAME #{numOfGames}")
    dealCard()
    
def option1():
    dealCard()

def option2():
    global dealerHand
    global numOfGames
    global hand
    global dealerWins
    global playerWins
    dealerHand = rng.next_int(11) + 26
    print(f"\nDealer's hand: {dealerHand}\nYour hand is: {hand}\n ")

    if(dealerHand > 21):
        print("Dealer exceeded 21! You win!")
        playerWins = playerWins + 1
        numOfGames = numOfGames + 1
        startGame()
    elif(hand > 21):
        print(f"\nYour card is a {cardName}!\nYour hand is: {hand}\n\nYou exceeded 21! You lose.\n")
        dealerWins = dealerWins + 1
        numOfGames = numOfGames + 1
        startGame()

    if(hand > dealerHand):
        print("You win!\n ")
    elif(hand < dealerHand):
        print("Dealer wins!\n ")
    elif(hand == dealerHand):
        print("It's a tie! No one wins!\n ")

    numOfGames = numOfGames + 1
    startGame()

def option3():
    percentageOfPlayerWins = round(playerWins / numOfGames, 1)
    print(f"Number of Player wins: {playerWins}\nNumber of Dealer wins: {dealerWins}\nNumber of tie games: {ties}\nTotal # of games played is: {numOfGames}\nPercentage of Player wins: {percentageOfPlayerWins}%\n ")
    printMenu()

def checkMenuSelection():
    global numOfGames
    global menuChoice
    if(menuChoice == "1"):
        option1()
    elif(menuChoice == "2"):
        option2()
    elif(menuChoice == "3"):
        option3()
    elif(menuChoice == "4"):
        exit()
    else:
        print(f"Invalid input!\nPlease enter an integer value between 1 and 4.")
        printMenu()

def exit():
    global gameExited
    gameExited = True

while gameExited == False:
    startGame()