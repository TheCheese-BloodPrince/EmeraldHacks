#intro
print("Hello, Welcome to connect 4! The goal of this game is to connect 4 of your coins in a row. Either vertical, horizontal, or diagonal\n")
#connect 4 board
columns = ["Column","1","2","3","4","5","6","7","8"]
r8 = ["Row8-->","_","_","_","_","_","_","_","_"]
r7 = ["Row7-->","_","_","_","_","_","_","_","_"]
r6 = ["Row6-->","_","_","_","_","_","_","_","_"]
r5 = ["Row5-->","_","_","_","_","_","_","_","_"]
r4 = ["Row4-->","_","_","_","_","_","_","_","_"]
r3 = ["Row3-->","_","_","_","_","_","_","_","_"]
r2 = ["Row2-->","_","_","_","_","_","_","_","_"]
r1 = ["Row1-->","_","_","_","_","_","_","_","_"]
#grid function will print out the grid every time called
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
#prints out grid
grid()
#setup
player1 = input("Enter name of player 1: ")
player2 = input("Enter name of player 2: ")
print("Player 1, " + player1 + ", will be X.")
print("Player 2, " + player2 + ", will be O.")
print()
grid()
#variables used later for identification
row = 0
row_num = 0
term_num = 0
column_num = str()
end_or_not = False
#player 1's turn
def p1():
    global row
    global row_num
    global column_num
    print("It's "+player1 + "'s turn")
    column_num = int(input("Enter column number: "))
    if column_num > 8 or column_num < 1:
        print("That column does not exist. Try again.")
        p1()
    elif r1[column_num] == "_":
        r1[column_num] = "X"
        row = r1
        row_num = 1
        grid()
    elif r2[column_num] == "_":
        r2[column_num] = "X"
        row = r2
        row_num = 2
        grid()  
    elif r3[column_num] == "_":
        r3[column_num] = "X"
        row = r3
        row_num = 3
        grid()  
    elif r4[column_num] == "_":
        r4[column_num] = "X"
        row = r4
        row_num = 4
        grid()  
    elif r5[column_num] == "_":
        r5[column_num] = "X"
        row = r5
        row_num = 5
        grid()  
    elif r6[column_num] == "_":
        r6[column_num] = "X"
        row = r6
        row_num = 6
        grid()  
    elif r7[column_num] == "_":
        r7[column_num] = "X"
        row = r7
        row_num = 7
        grid()  
    elif r8[column_num] == "_":
        r8[column_num] = "X"
        row = r8
        row_num = 8
        grid() 
    else: 
        print("There are no more spaces left in column number " + str(column_num))
        p1()
#player 2's turn 
def p2():
    global row
    global row_num
    global column_num
    print("It's "+player2 + "'s turn")
    column_num = int(input("Enter column number: "))
    if column_num > 8 or column_num < 1:
        print("That column does not exist. Try again.")
        p2()
    elif r1[column_num] == "_":
        r1[column_num] = "O"
        row = r1
        row_num = 1
        grid()
    elif r2[column_num] == "_":
        r2[column_num] = "O"
        row = r2
        row_num = 2
        grid()  
    elif r3[column_num] == "_":
        r3[column_num] = "O"
        row = r3
        row_num = 3
        grid()  
    elif r4[column_num] == "_":
        r4[column_num] = "O"
        row = r4
        row_num = 4
        grid()  
    elif r5[column_num] == "_":
        r5[column_num] = "O"
        row = r5
        row_num = 5
        grid()  
    elif r6[column_num] == "_":
        r6[column_num] = "O"
        row = r6
        row_num = 6
        grid()  
    elif r7[column_num] == "_":
        r7[column_num] = "O"
        row = r7
        row_num = 7
        grid()  
    elif r8[column_num] == "_":
        r8[column_num] = "O"
        row = r8
        row_num = 8
        grid() 
    else: 
        print("There are no more spaces left in column number " + str(column_num)) 
        p2()

while True:
    #player 1's move
    p1()
    #assigns vertical columns to variables
    c1 = [r1[1],r2[1],r3[1],r4[1],r5[1],r6[1],r7[1],r8[1]]
    c2 = [r1[2],r2[2],r3[2],r4[2],r5[2],r6[2],r7[2],r8[2]]
    c3 = [r1[3],r2[3],r3[3],r4[3],r5[3],r6[3],r7[3],r8[3]]
    c4 = [r1[4],r2[4],r3[4],r4[4],r5[4],r6[4],r7[4],r8[4]]
    c5 = [r1[5],r2[5],r3[5],r4[5],r5[5],r6[5],r7[5],r8[5]]
    c6 = [r1[6],r2[6],r3[6],r4[6],r5[6],r6[6],r7[6],r8[6]]
    c7 = [r1[7],r2[7],r3[7],r4[7],r5[7],r6[7],r7[7],r8[7]] 
    c8 = [r1[8],r2[8],r3[8],r4[8],r5[8],r6[8],r7[8],r8[8]]   
    connect4 = 0
    #checks for horizontal connect 4
    for term in r1:
        if term == "X":
            connect4 += 1
            if connect4 == 4:
                print(player1 + " wins.")
                exit()
        else:
            connect4 = 0
    for term in r2:
        if term == "X":
            connect4 += 1
            if connect4 == 4:
                print(player1 + " wins.")
                exit()
        else:
            connect4 = 0
        
    for term in r3:
        if term == "X":
            connect4 += 1
            if connect4 == 4:
                print(player1 + " wins.")
                exit()
        else:
            connect4 = 0
    for term in r4:
        if term == "X":
            connect4 += 1
            if connect4 == 4:
                print(player1 + " wins.")
                exit()
        else:
            connect4 = 0
    for term in r5:
        if term == "X":
            connect4 += 1
            if connect4 == 4:
                print(player1 + " wins.")
                exit()
        else:
            connect4 = 0
    for term in r6:
        if term == "X":
            connect4 += 1
            if connect4 == 4:
                print(player1 + " wins.")
                exit()
        else:
            connect4 = 0
    for term in r7:
        if term == "X":
            connect4 += 1
            if connect4 == 4:
                print(player1 + " wins.")
                exit()
        else:
            connect4 = 0
    for term in r8:
        if term == "X":
            connect4 += 1
            if connect4 == 4:
                print(player1 + " wins.")
                exit()
        else:
            connect4 = 0
    #checks for vertical connect 4
    for term in c1:
        if term == "X":
            connect4 += 1
            if connect4 == 4:
                print(player1  + " wins.")
                exit()
        else:
            connect4 = 0
    for term in c2:
        if term == "X":
            connect4 += 1
            if connect4 == 4:
                print(player1  + " wins.")
                exit()
        else:
            connect4 = 0
    for term in c3:
        if term == "X":
            connect4 += 1
            if connect4 == 4:
                print(player1  + " wins.")
                exit()
        else:
            connect4 = 0
    for term in c4:
        if term == "X":
            connect4 += 1
            if connect4 == 4:
                print(player1  + " wins.")
                exit()
        else:
            connect4 = 0
    for term in c5:
        if term == "X":
            connect4 += 1
            if connect4 == 4:
                print(player1  + " wins.")
                exit()
        else:
            connect4 = 0
    for term in c6:
        if term == "X":
            connect4 += 1
            if connect4 == 4:
                print(player1  + " wins.")
                exit()
        else:
            connect4 = 0
    for term in c7:
        if term == "X":
            connect4 += 1
            if connect4 == 4:
                print(player1  + " wins.")
                exit()
        else:
            connect4 = 0
    for term in c8:
        if term == "X":
            connect4 += 1
            if connect4 == 4:
                print(player1  + " wins.")
                exit()
        else:
            connect4 = 0
    #check for horizontal connect 4
    term_num=0
    connect4list = [c1,c2,c3,c4,c5,c6,c7,c8]
    connect4shortenedlist = [c1,c2,c3,c4,c5]
    for term in connect4shortenedlist:
        term_num += 1
        for i in term:
            if i == "X":
                try:
                    if i[term_num][term_num] == "X":
                        try: 
                            if c3[term_num + 1] == "X":
                                try:
                                    if c3[term_num + 1] == "X":
                                        print(player1+" wins.")
                                        end_or_not = True
                                    break
                                except:
                                    pass
                        except:
                            pass    
                except: 
                    pass 
    if end_or_not == True:
        end()   
    #player two's move
    p2()
    #assigns vertical columns to variables
    c1 = [r1[1],r2[1],r3[1],r4[1],r5[1],r6[1],r7[1],r8[1]]
    c2 = [r1[2],r2[2],r3[2],r4[2],r5[2],r6[2],r7[2],r8[2]]
    c3 = [r1[3],r2[3],r3[3],r4[3],r5[3],r6[3],r7[3],r8[3]]
    c4 = [r1[4],r2[4],r3[4],r4[4],r5[4],r6[4],r7[4],r8[4]]
    c5 = [r1[5],r2[5],r3[5],r4[5],r5[5],r6[5],r7[5],r8[5]]
    c6 = [r1[6],r2[6],r3[6],r4[6],r5[6],r6[6],r7[6],r8[6]]
    c7 = [r1[7],r2[7],r3[7],r4[7],r5[7],r6[7],r7[7],r8[7]] 
    c8 = [r1[8],r2[8],r3[8],r4[8],r5[8],r6[8],r7[8],r8[8]]
    #loops through each row to see if there is a horizontal connect 4
    for term in r1:
        if term == "O":
            connect4 += 1
            if connect4 == 4:
                print(player2 + " wins.")
                exit()
        else:
            connect4 = 0
    for term in r2:
        if term == "O":
            connect4 += 1
            if connect4 == 4:
                print(player2 + " wins.")
                exit()
        else:
            connect4 = 0
    for term in r3:
        if term == "O":
            connect4 += 1
            if connect4 == 4:
                print(player2 + " wins.")
                exit()
        else:
            connect4 = 0
    for term in r4:
        if term == "O":
            connect4 += 1
            if connect4 == 4:
                print(player2 + " wins.")
                exit()
        else:
            connect4 = 0
    for term in r5:
        if term == "O":
            connect4 += 1
            if connect4 == 4:
                print(player2 + " wins.")
                exit()
        else:
            connect4 = 0
    for term in r6:
        if term == "O":
            connect4 += 1
            if connect4 == 4:
                print(player2 + " wins.")
                exit()
        else:
            connect4 = 0
    for term in r7:
        if term == "O":
            connect4 += 1
            if connect4 == 4:
                print(player2 + " wins.")
                exit()
        else:
            connect4 = 0
    for term in r8:
        if term == "O":
            connect4 += 1
            if connect4 == 4:
                print(player2 + " wins.")
                exit()
        else:
            connect4 = 0
    #checks for vertical connect 4
    for term in c1:
        if term == "O":
            connect4 += 1
            if connect4 == 4:
                print(player2 + " wins.")
                exit()
        else:
            connect4 = 0
    for term in c2:
        if term == "O":
            connect4 += 1
            if connect4 == 4:
                print(player2 + " wins.")
                exit()
        else:
            connect4 = 0
    for term in c3:
        if term == "O":
            connect4 += 1
            if connect4 == 4:
                print(player2 + " wins.")
                exit()
        else:
            connect4 = 0
    for term in c4:
        if term == "O":
            connect4 += 1
            if connect4 == 4:
                print(player2 + " wins.")
                exit()
        else:
            connect4 = 0
    for term in c5:
        if term == "O":
            connect4 += 1
            if connect4 == 4:
                print(player2 + " wins.")
                exit()
        else:
            connect4 = 0
    for term in c6:
        if term == "O":
            connect4 += 1
            if connect4 == 4:
                print(player2 + " wins.")
                exit()
        else:
            connect4 = 0
    for term in c7:
        if term == "O":
            connect4 += 1
            if connect4 == 4:
                print(player2 + " wins.")
                exit()
        else:
            connect4 = 0
    for term in c8:
        if term == "O":
            connect4 += 1
            if connect4 == 4:
                print(player2 + " wins.")
                exit()
        else:
            connect4 = 0
    #check for horizontal connect 4