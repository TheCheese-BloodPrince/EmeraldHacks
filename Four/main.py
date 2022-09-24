import random

print("Welcome to Battleship! Your objective is to sink all of the enemy's ships.\nThere's one 2-spaced ship and one 3-spaced ship hidden below the surface.\n")
dRow = list()
for i in range(10):
    dRow.append("-")
gridLayout = list()
for i in range(10):
    gridLayout.append(dRow)

def layout():
    for i in gridLayout:
        eRow = ""
        for j in i:
            eRow += j
            eRow += " "
        print(eRow)
layout()

numberOfTry = 0
numberOfHits = 0
numberOfSquares = 5


fRow = list()
for i in range(10):
    fRow.append(False)
shipArray = list()
for i in range(10):
    shipArray.append(fRow)


randStartRow = random.randint(0,9)
randStartCol = random.randint(0,9)
storeShip1Row = random.randint(0,9)
storeShip1Col = random.randint(0,9)

shipArray[storeShip1Row][randStartCol] = True
shipArray[randStartRow][storeShip1Col] = True

if storeShip1Row == 9:
    storeShip1Row -= 1
    shipArray[storeShip1Row][randStartCol] = True
else:
    storeShip1Row += 1
    shipArray[storeShip1Row][randStartCol] = True


if (storeShip1Col + 3 <= 9):
    shipArray[randStartRow][storeShip1Col+1] = True
    shipArray[randStartRow][storeShip1Col+2] = True
else:
    shipArray[randStartRow][storeShip1Col-1] = True
    shipArray[randStartRow][storeShip1Col-2] = True


while numberOfHits != numberOfSquares:
    print("\nPick a row:\n")
    rowInput = int(input())
    print("\nPick a column:\n")
    columnInput = int(input())
    if (rowInput > 9 or rowInput < 0 or columnInput > 9 or columnInput < 0):
        print("\nPick a row:\n")
        rowInput = int(input())
        print("\nPick a column:\n")
        columnInput = int(input())

    if (shipArray[rowInput][columnInput] == True):
        print("It's a hit!")
        numberOfHits += 1
        gridLayout[rowInput][columnInput] = True
    else:
        print("It's a miss!")
        layout()
        numberOfTry += 1
    
    if (numberOfHits == numberOfSquares):
        break

