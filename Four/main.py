oceanrow = list()
for i in range(10):
    oceanrow.append("-")

ocean = [["F", "-", "G", "-", "H", "-", "I", "-", "J", "-"]]
for i in range(8):
    ocean.append(oceanrow)
ocean.append(["A", "-", "B", "-", "C", "-", "D", "-", "E", "-"])

playerview = ocean
playerview[0] = oceanrow

playerShips = ["A","B","C","D","E"]
AIships = ["F","G","H","I","J"]

def playerTurn():
    print("Would you like to:\n[1] Move a Ship\n[2] Attack")
    choice = int(input())
    if choice == 1:
        print("Which ship would you like to move?")
        for i in playerShips:
            print(i)
        ship = input()
        if not ship in playerShips:
            print("Invalid Input")
            playerTurn()
        
        print("Would you like to move the ship:\n[U] Up\n[R] Right\n[D] Down\n[L] Left")
        movement = input()

        for i in range(ocean.size()):
            for j in i:
                if j == ship:
                    shipPos = [i,j]
        
        i = shipPos[0]
        j = shipPos[1]
        print(type(i))

        if movement == "U" and i<9 and ocean[i+1][j] == "-":
            ocean[i][j] = "-"
            ocean[i+1][j] = ship
            playerview[i][j] = "-"
            playerview[i+1][j] = ship

        elif movement == "R" and j<9 and ocean[i][j+1] == "-":
            ocean[i][j] = "-"
            ocean[i][j+1] = ship
            playerview[i][j] = "-"
            playerview[i][j+1] = ship
        elif movement == "D" and i>0 and ocean[i-1][j] == "-":
            ocean[i][j] = "-"
            ocean[i-1][j] = ship
            playerview[i][j] = "-"
            playerview[i-1][j] = ship
        elif movement == "L" and j>0 and ocean[i][j-1] == "-":
            ocean[i][j] = "-"
            ocean[i][j-1] = ship
            playerview[i][j] = "-"
            playerview[i][j-1] = ship
        else:
            print("Invalid Input")
            playerTurn()
    else:
        print("What row would you like to attack?(0-9)")
        row = int(input())
        print("What column would you like to attack(0-9)")
        column = int(input())

        if not (row >= 0 and row <= 9 and column >= 0 and column <= 9):
            print("Invalid Input")
            playerTurn()
        
        for k in AIships:
            if ocean[i][j] == k:
                ocean[i][j] = "-"
                print("You sunk opponent's ship: " + AIships[k])
                AIships.remove(k)

        


def display():
    for l in playerview:
        e = " "
        for k in l:
            e += k
            e += " "
        print(e)

while True:
    print(playerview)
    display()
    playerTurn()