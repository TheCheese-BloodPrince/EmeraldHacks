print("Hello, Welcome to connect 4! The goal of this game is to connect 4 of your coins in a row. Either vertical, horizontal, or diagonal\n")
columns = ["Column","1","2","3","4","5","6","7","8"]
r8 = ["Row8-->","_","_","_","_","_","_","_","_"]
r7 = ["Row7-->","_","_","_","_","_","_","_","_"]
r6 = ["Row6-->","_","_","_","_","_","_","_","_"]
r5 = ["Row5-->","_","_","_","_","_","_","_","_"]
r4 = ["Row4-->","_","_","_","_","_","_","_","_"]
r3 = ["Row3-->","_","_","_","_","_","_","_","_"]
r2 = ["Row2-->","_","_","_","_","_","_","_","_"]
r1 = ["Row1-->","_","_","_","_","_","_","_","_"]
def grid():
    print("Here is the grid: \n")
    print(columns)
    print(r8)
    print(r7)
    print(r6)
    print(r5)
    print(r4)
    print(r3)
    print(r2)
    print(r1)
    print()
grid()
player1 = input("Enter name of player 1: ")
player2 = input("Enter name of player 2: ")
print("Player 1, " + player1 + ", will be X.")
print("Player 2, " + player2 + ", will be O.")
print()

def p1():
    print("It's "+player1 + "'s turn")
    column_num = int(input("Enter column number: "))
    if r1[column_num] == "_":
        r1[column_num] = "X"
        grid()
    elif r2[column_num] == "_":
        r2[column_num] = "X"
        grid()  
    elif r3[column_num] == "_":
        r3[column_num] = "X"
        grid()  
    elif r4[column_num] == "_":
        r4[column_num] = "X"
        grid()  
    elif r5[column_num] == "_":
        r5[column_num] = "X"
        grid()  
    elif r6[column_num] == "_":
        r6[column_num] = "X"
        grid()  
    elif r7[column_num] == "_":
        r7[column_num] = "X"
        grid()  
    elif r8[column_num] == "_":
        r8[column_num] = "X"
        grid() 
    else: 
        print("There are no more spaces left in column number " + str(column_num))
        p1()
def p2():
    print("It's "+player2 + "'s turn")
    column_num = int(input("Enter column number: "))
    if r1[column_num] == "_":
        r1[column_num] = "O"
        grid()
    elif r2[column_num] == "_":
        r2[column_num] = "O"
        grid()  
    elif r3[column_num] == "_":
        r3[column_num] = "O"
        grid()  
    elif r4[column_num] == "_":
        r4[column_num] = "O"
        grid()  
    elif r5[column_num] == "_":
        r5[column_num] = "O"
        grid()  
    elif r6[column_num] == "_":
        r6[column_num] = "O"
        grid()  
    elif r7[column_num] == "_":
        r7[column_num] = "O"
        grid()  
    elif r8[column_num] == "_":
        r8[column_num] = "O"
        grid() 
    else: 
        print("There are no more spaces left in column number " + str(column_num)) 
        p2()

while True:
    p1()
    p2()