oceanrow = list()
for i in range(10):
    oceanrow.append("-")

ocean = [["F", "-", "G", "-", "H", "-", "I", "-", "J", "-"]]
for i in range(8):
    ocean.append(oceanrow)
oceanrow.append("A", "-", "B", "-", "C", "-", "D", "-", "E", "-")

playerview = list()
for i in range(9):
    playerview.append(oceanrow)

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
        
        print("Would you like to move the ship:\n[1] Up\n[2] Right\n[3] Down\n[4] Left")
        movement = int(input())

        for i in ocean:
            for j in i:
                if j == ship:
                    shipPos = [i,j]
        
        i = shipPos[0]
        j = shipPos[1]

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



while True:
