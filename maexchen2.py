import random

#all the combinations possible
results = [[3,1],[3,2],[4,1],[4,2],[4,3],[5,1],[5,2],[5,3],[5,4],[6,1],[6,2],[6,3],[6,4],[6,5],[3,1],[3,2],[4,1],[4,2],[4,3],[5,1],[5,2],[5,3],[5,4],[6,1],[6,2],[6,3],[6,4],[6,5],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[2,1],[2,1]]

def myTurn():
    lie = False
    #Returns one Element from the results array == dice throw
    myThrow = results[random.randint(1,20)]
    #returns the index of myThrow, used for calculation
    myResult = results.index(myThrow)
    print(myThrow)
    lie = input("Lügen? Ja / Nein: ") 
    #Win instantly if you get a maexchen
    if(myResult == 20):
        print("Maexchen! You Win!")
        quit()
    
    elif (lie == "Ja"):
        lie = True
        myDice1 = int(input("Würfel 1 eingeben: "))
        myDice2 = int(input("Würfel 2 eingeben: "))
        myThrow = [myDice1, myDice2]
        myResult = results.index(myThrow)
        return myResult, lie
    else:
        return myResult,lie

#Checks if a player lied
def checkLie(lie):
    if (lie == True):
        return True
    else:
        return False

def compTurn(myResult, lie):
    probability = random.randint(1,10)
    if(probability <= 5):
        if(checkLie(lie)):
            print("You lied! You loose...")
            quit()
        else:
            print("You told the truth. You won!")
            quit()
    else:
        compThrow = results[random.randint(1,20)]
        compResult = results.index(compThrow)
        compLie = False
        if(compResult == 20):
            print("Maexchen! Computer won!")
            quit()
        elif (compResult < myResult):
            compLie = True
            return results[myResult + 1], compLie
        else:
            return compThrow, compLie

def maexchen():
    winner = False
    while(winner == False):
        myResult, lie = myTurn()
        compResult, compLie = compTurn(myResult, lie)
        print(compResult)
        trust = input("Glauben? Nein / Ja: ")
        if(trust == "Nein"):
            if(checkLie(compLie)):
                print("Computer lied! You win!")
                quit()
            else:
                print("Computer told the truth! You loose...")
                quit()

    print("The Computer was better than you! Looser...")
    quit()

if __name__ == "__main__":
    maexchen()