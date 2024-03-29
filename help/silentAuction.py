from os import system

def maxy(dictData):
    
    winnerBid = 0
    winner = "" 
    for key in dictData:
        value = dictData[key]
        if value > winnerBid:
            winner = key
            winnerBid = value
    print(f"The winner is {winner} with a bid of ${winnerBid}")

bidData = {}

gameover = False
while not gameover:
    
    system("cls")
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    
    bidData[name] = bid

    bidder = input("Are there any other bidders? Type 'yes or 'no'.").lower()


    if bidder == "no":
        gameover = True



maxy(bidData)
print(bidData)

