#my name= Salih Eren Yüzbaşıoğlu ID=2220356040
def print_and_output(strng):
    # Get the global output file
    global output

    # Print the string and write it to the output file
    print(strng, end=""),output.write(strng)
def inputreading():
    # Import sys module and global variables
    import sys
    global player1list, player2list, player1moves, player2moves, output, wronginput

    # Initialize error message and output file
    errorstring, output = "IOError: input file(s) ", open("Battleship.out", "w")

    # Try to read player 1 input file
    try:
        player1 = open(sys.argv[1]).readlines()
    except IOError:
        # If file not found, add to error message
        errorstring += "Player1.txt, "

    # Try to read player 2 input file
    try:
        player2 = open(sys.argv[2]).readlines()
    except IOError:
        # If file not found, add to error message
        errorstring += "Player2.txt, "

    # Try to read player 1 moves file
    try:
        player1moves = open(sys.argv[3]).readline().strip(";").split(";")
    except IOError:
        # If file not found, add to error message
        errorstring += "Player1.in, "

    # Try to read player 2 moves file
    try:
        player2moves = open(sys.argv[4]).readline().strip(";").split(";")
    except IOError:
        # If file not found, add to error message
        errorstring += "Player2.in, "

    # If any files were not found, print error message and raise IOError exception
    if len(errorstring) > 23:
        print_and_output(errorstring[:-2] + " is/are not reachable.")
        raise IOError

    # Initialize empty lists and counter
    player1list, player2list, wronginput, shipcount = [], [], [0, 0], 0
    def Playerlist(player,playerlist):
          for row in player:
              values = row.split(";")  # Split the row by the semicolon character and store the resulting list in a new variable
              values = [value[0] if (value and value!="\n") else "-" for value in values]  # Replace any empty values with dashes
              playerlist.append(values)  # Add the list to the playerlist
    Playerlist(player1,player1list),Playerlist(player2,player2list)
    print_and_output("Battle of Ships Game\n\n")
def shipfinder(playerlist):
    # List of ships to find
    to_find = ["B14", "B24", "P42", "P32", "P12", "P22"]

    # Loop through each element in player list
    for toFind in to_find:
        for i in range(10):
            for j in range(10):
                m = 0
                # If element matches first character of ship to find
                if playerlist[i][j] == toFind[0]:
                    # Check surrounding elements for potential ship
                    for k, b in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                        try:
                            # If element in direction (k, b) is also first character of ship to find
                            # and element two steps in that direction is also the first character (for P ships) or the element two steps in that direction does not exist (for other ships)
                            if playerlist[i + k][j + b] == toFind[0] and (playerlist[i + k * 2][j + b * 2] == toFind[0] or toFind[0] == "P"):
                                # Increment counter and store direction
                                m += 1
                                r = (k, b)
                        # Ignore index errors (i.e. element does not exist)
                        except:
                            pass
                    # If only one direction was found
                    if m == 1:
                        # Replace current element and all elements in that direction with ship identifier
                        playerlist[i][j] = toFind[:2]
                        for t in range(1, int(toFind[-1])):
                            playerlist[i + t * r[0]][j + t * r[1]] = toFind[:2]
                        # Break out of inner loop
                        break
            # Break out of outer loop if ship was found
            if m == 1:
                break

    global ships,letters# glabal ships variable used to store ship's healty squares
    ships,letters={},{}#letters are used to find the corresponding index
    ships["B1_1"],ships["B2_1"],ships["B2_2"],ships["B1_2"],ships["P3_1"],ships["P4_1"],ships["P3_2"],ships["P4_2"],ships["P1_1"],ships["P2_1"],ships["P1_2"],ships["P2_2"],ships["C_1"],ships["C_2"],ships["D_1"],ships["D_2"],ships["S_1"],ships["S_2"]=4,4,4,4,2,2,2,2,2,2,2,2,5,5,3,3,3,3
    letters["A"],letters["B"],letters["C"],letters["D"],letters["E"],letters["F"],letters["G"],letters["H"],letters["I"],letters["J"]=0,1,2,3,4,5,6,7,8,9
    shipcount=0
    for line in playerlist:#making sure there are right amount of ships
        for element in line:
            if element!="-":
                shipcount+=1
    if shipcount!=27:
        assert AssertionError
def gameOutput(Turn):
    try:
        def player1or2(z):
            global wronginput
            if z==2:#changing variables depending on the which player is playing
                player="_1"
                global player2moves
                turnmoves=player2moves#moves of the playing player
                global player1list
                notturnlist=player1list#list of the not playing player
            else:
                player="_2"
                global player2list
                notturnlist=player2list#list of the not playing player

                global player1moves
                turnmoves=player1moves#moves of the playing player
            print_and_output(f"Player{z}'s Move\n\n")#printing necessery information
            print_and_output(f"Round : {Turn}\t\t\t\t\tGrid Size: 10x10\n\n")
            print_and_output("Player1's Hidden Board\t\tPlayer2's Hidden Board\n")
            print_and_output("  A B C D E F G H I J\t\t  A B C D E F G H I J\n")
            # Loop through each row in the board
            for i in range(10):
                # Call print_and_output function to print row number
                print_and_output(f"{i + 1}")

                # Loop through each column in the row
                for j in range(10):
                    # Check if the current cell contains an O or X, otherwise use a dash
                    toprint = (player1list[i][j][0] == "O") * "O" or (player1list[i][j][0] == "X") * "X" or "-"
                    # Call print_and_output function to print the cell value, adding extra space if it's not the last cell in the row
                    print_and_output(" " * (i != 9 or j != 0) + f"{toprint}")
                # Call print_and_output function to print tab characters
                print_and_output("\t\t")

                # Repeat the same process for player 2's board
                print_and_output(f"{i + 1}")
                for j in range(10):
                    toprint = (player2list[i][j][0] == "O") * "O" or (player2list[i][j][0] == "X") * "X" or "-"
                    print_and_output(" " * (i != 9 or j != 0) + f"{toprint}")
                # Call print_and_output function to print a newline character
                print_and_output("\n")

            # Call print_and_output function to print a newline character
            print_and_output("\n")

            # Loop through each ship
            for j in [["C"], ["B1", "B2"], ["D"], ["S"], ["P1", "P2", "P3", "P4"]]:
                # Initialize empty strings to store the status of each ship
                ship_1, ship_2 = "", ""

                # Loop through each part of the ship
                for k in j:
                    # Check if the ship has been sunk (value of 0) and add an X to the string, otherwise add a dash
                    ship_1 = (ships[k + "_1"] == 0) * ("X " + ship_1) or ship_1 + "- "
                    ship_2 = (ships[k + "_2"] == 0) * ("X " + ship_2) or ship_2 + "- "

                # Determine the name of the ship based on the first letter of its identifier
                ship = "Carrier" * (k[0] == "C") or "Battleship" * (k[0] == "B") or "Destroyer" * (
                            k[0] == "D") or "Submarine" * (k[0] == "S") or "Patrol Boat" * (k[0] == "P")
                # Determine the number of tabs to print based on the name of the ship
                tabNumber = "\t" * 2 * (k[0] == "C") or "\t"
                tabNumber2 = "\t" * 3 * (k[0] == "P") or "\t\t\t\t"
                # Call print_and_output function to print the ship's name and status
                print_and_output(f"{ship}{tabNumber}{ship_1[:-1]}{tabNumber2}{ship}{tabNumber}{ship_2[:-1]}\n")
            print_and_output("\n")

            while True:#this part checks if move is correct or not until it is correct
                move1 = turnmoves[Turn - 1+wronginput[z-1]]
                print_and_output(f"Enter your move: {move1}\n\n")


                move=move1.split(",")
                if len(move)==1:#if there are no "," in move
                    print_and_output(f"IndexError: move should have ',' in it.\n\n")
                    wronginput[z-1]+=1
                    continue

                if len(move)!=2:#if there are moren then 1 , in move
                    print_and_output(f"ValueError: {move1} should have single ',' in it.\n\n")
                    wronginput[z - 1] += 1
                    continue
                if move[0]=="" or move[1]=="":#these are obvious
                    print_and_output(f"IndexError: {move1} should have a number between 1 and 10 and a letter in it.\n\n")
                    wronginput[z - 1] += 1#making sure it does not iterate over same move
                    continue
                try:
                    if int(move[0]):
                        pass
                except:
                    print_and_output(f"IndexError: {move1} should start with a number between 1 and 10.\n\n")
                    wronginput[z - 1] += 1
                    continue
                if (int(move[0]) < 1 or int(move[0]) > 10):
                    print_and_output("AssertionError: Invalid Operation.\n\n")
                    wronginput[z - 1] += 1
                    continue
                if move[1] not in letters:
                    print_and_output("AssertionError: Invalid Operation.\n\n")
                    wronginput[z - 1] += 1
                    continue
                if notturnlist[int(move[0])-1][letters[move[1]]][0]=="X" or notturnlist[int(move[0])-1][letters[move[1]]][0]=="O":
                    print_and_output("AssertionError: Invalid Operation.\n\n")
                    wronginput[z - 1] += 1
                    continue

                break


            if notturnlist[int(move[0])-1][letters[move[1]]]!="-":#decreasing the ship if it is a hit
                ships[notturnlist[int(move[0]) - 1][letters[move[1]]]+player]-=1

            #changing the player that got hit's list so it is either "X" or "O"
            notturnlist[int(move[0])-1][letters[move[1]]]=(notturnlist[int(move[0])-1][letters[move[1]]]=="-")*"O" or "X"+notturnlist[int(move[0])-1][letters[move[1]]]

        def finalGame(z):
            # Print either a draw or the winner, depending on the value of z
            print_and_output((z == 3) * "It is a Draw!\n\n" or f"Player{z} Wins!\n\n")

            # Print final information header
            print_and_output("Final Information\n\n")

            # Print player 1's and player 2's boards
            print_and_output("Player1's Board\t\t\t\tPlayer2's Board\n")

            # Print the top row with column labels
            print_and_output("  A B C D E F G H I J\t\t  A B C D E F G H I J\n")

            # Iterate through rows and columns of both player's boards
            for i in range(10):
                # Print the row number
                print_and_output(f"{i + 1}")
                for j in range(10):
                    # Print the value at the current position in player 1's board
                    toprint = player1list[i][j][0]
                    # Add a space if this is not the last row
                    print_and_output(" " * (i != 9 or j != 0) + f"{toprint}")
                # Print a tab separator between the two boards
                print_and_output("\t\t")
                # Print the row number again
                print_and_output(f"{i + 1}")
                for j in range(10):
                    # Print the value at the current position in player 2's board
                    toprint = player2list[i][j][0]
                    # Add a space if this is not the last row
                    print_and_output(" " * (i != 9 or j != 0) + f"{toprint}")
                # Print a newline character
                print_and_output("\n")

            # Print another newline character
            print_and_output("\n")

            # Iterate through each type of ship
            for j in [["C"], ["B1", "B2"], ["D"], ["S"], ["P1", "P1", "P3", "P4"]]:
                # Initialize variables to store the number of each ship remaining for player 1 and player 2
                ship_1, ship_2 = "", ""
                for k in j:
                    # If the ship has been sunk for player 1, add an "X" to the string. Otherwise, add a "-".
                    ship_1 = (ships[k + "_1"] == 0) * ("X " + ship_1) or ship_1 + "- "
                    # If the ship has been sunk for player 2, add an "X" to the string. Otherwise, add a "-".
                    ship_2 = (ships[k + "_2"] == 0) * ("X " + ship_2) or ship_2 + "- "
                # Determine the name of the ship
                ship="Carrier"*(k[0]=="C") or "Battleship"*(k[0]=="B") or "Destroyer"*(k[0]=="D") or "Submarine"*(k[0]=="S") or "Patrol Boat"*(k[0]=="P")
                tabNumber="\t"*2*(k[0]=="C") or "\t"
                tabNumber2="\t"*3*(k[0]=="P") or "\t\t\t\t"
                print_and_output(f"{ship}{tabNumber}{ship_1[:-1]}{tabNumber2}{ship}{tabNumber}{ship_2[:-1]}\n")
            raise IndexError
        player1or2(1)# player 1 playing it's turn
        sumplayer1=0
        sumplayer2=0#amount of ship squares that is left
        for i in ships:
            if i[-1]=="1":
                sumplayer1+=ships[i]
            else:
                sumplayer2+=ships[i]#finding them
        if sumplayer2==0:#if player 2 has no ships left we have either declare draw or win for player 1
            if sumplayer1==1:#this means there can be a draw
                player1or2(2)#so we allow player 2 to play
                sumplayer1 = 0
                for i in ships:# and then we check if player 2 did hit or not
                    if i[-1]=="1":
                        sumplayer1 += ships[i]
                if sumplayer1==0:#if it did we declare draw
                    finalGame(3)
                else:
                    finalGame(1)#if not we declare win for player1
            else:
                finalGame(1)#if there are more than 1 ship we dont even give player 2 a chance
        else:
            player1or2(2)# if there are more than o ships for player 2 the goes normally
            sumplayer1 = 0
            for i in ships:

                if i[-1] == "1":
                    sumplayer1 += ships[i]#again checking ship count


            if sumplayer1==0:
                finalGame(2)# this means win for player 2
        gameOutput(Turn+1)#next turn
    except IndexError:# this only works if game does'not end with a draw or a win but instead there are not any moves left
        pass

try:
    inputreading(),shipfinder(player1list),shipfinder(player2list),gameOutput(1)# we call this functions to start and end the game
except IOError:# this happpens when files are not reacheable
    pass
except:#if there is any error we could not do this happens
 print_and_output(" kaBOOM: run for your life!")