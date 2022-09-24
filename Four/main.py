print("Welcome to Battleship! Your objective is to sink all of the enemy's ships.\nThere are 5 ships; A Destroyer(2 Squares), a Cruiser(3 Squares), a Submarine(3 Squares), a Battleship(4 Squares), and an Aircraft Carrier(5 Squares)\n")

def ship_setup(destroyerOri, destroyerPos, cruiserOri, cruiserPos, submarineOri, submarinePos, battleshipOri, battleshipPos, carrierOri, carrierPos):
    shipRow = list()
    for i in range(10):
        shipRow.append("N")
    ships = list()
    for i in range(10):
        ships.append(shipRow)
    
    def posShip(ori, pos, length):
        