board = [["-", "-", "-"],
         ["-", "-", "-"],
         ["-", "-", "-"]
         ]
valid = [0,1,2]
player_1_turns = [1,3,5,7,9]
player_2_turns = [2,4,6,8]

# practice = [["A", "B", "C"],
#             ["D", "E", "F"],
#             ["G", "H", "I"]
#             ]
#
# column_0 = [board[0][0], board[1][0], board[2][0]]
# column_1 = [board[0][1], board[1][1], board[2][1]]
# column_2 = [board[0][2], board[1][2], board[2][2]]



def make_board():
    return [["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"]
             ]
def change_board_1(row, column):
    board[row][column] = "X"
    return board
def change_board_2(row, column):
    board[row][column] = "O"
    return board
def show_board(board):
    for line in board:
        print(line)

def player_1_choice_row():
    player_1_row = "start"
    while player_1_row not in valid:
        player_1_row = int(input("Choose a row for an X:   "))
    return player_1_row

def player_1_choice_column():
    player_1_column = "start"
    while player_1_column not in valid:
        player_1_column = int(input("Choose a column for an X:   "))
    return player_1_column

def player_2_choice_row():
    player_2_row = "start"
    while player_2_row not in valid:
        player_2_row = int(input("Choose a row for an O:   "))
    return player_2_row

def player_2_choice_column():
    player_2_column = "start"
    while player_2_column not in valid:
        player_2_column = int(input("Choose a column for an O:   "))
    return player_2_column

def player_1_turn():
    print("PLAYER 1 it is your turn \n")
    row = player_1_choice_row()
    column = player_1_choice_column()
    if board[row][column] == "-":
        change_board_1(row, column)
        show_board(board)
    else:
        print("That spot is taken")
        player_1_turn()

def player_2_turn():
    print("PLAYER 2 it is your turn \n")
    row = player_2_choice_row()
    column = player_2_choice_column()
    if board[row][column] == "-":
        change_board_2(row, column)
        show_board(board)
    else:
        print("That spot is taken")
        player_2_turn()

def check_winner():
    column_0 = [board[0][0], board[1][0], board[2][0]]
    column_1 = [board[0][1], board[1][1], board[2][1]]
    column_2 = [board[0][2], board[1][2], board[2][2]]
    diagonal_a = [board[0][0], board[1][1], board[2][2]]
    diagonal_b = [board[0][2], board[1][1], board[2][0]]
    # print(column_0, column_1, column_2)
    # print(board[0], board[1], board[2])

    if "X" not in board[0] and "-" not in board[0]:
        print("Player 2 Wins")
        return True
    elif "O" not in board[0] and "-" not in board[0]:
        print("Player 1 Wins")
        return True
    elif "X" not in board[1] and "-" not in board[1]:
        print("Player 2 Wins")
        return True
    elif "O" not in board[1] and "-" not in board[1]:
        print("Player 1 Wins")
        return True
    elif "X" not in board[2] and "-" not in board[2]:
        print("Player 2 Wins")
        return True
    elif "O" not in board[2] and "-" not in board[2]:
        print("Player 1 Wins")
        return True
    elif "X" not in column_0 and "-" not in column_0:
        print("Player 2 Wins")
        return True
    elif "O" not in column_0 and "-" not in column_0:
        print("Player 1 Wins")
        return True
    elif "X" not in column_1 and "-" not in column_1:
        print("Player 2 Wins")
        return True
    elif "O" not in column_1 and "-" not in column_1:
        print("Player 1 Wins")
        return True
    elif "X" not in column_2 and "-" not in column_2:
        print("Player 2 Wins")
        return True
    elif "O" not in column_2 and "-" not in column_2:
        print("Player 1 Wins")
        return True
    elif "O" not in diagonal_a and "-" not in diagonal_a:
        print("Player 1 Wins")
        return True
    elif "X" not in diagonal_a and "-" not in diagonal_a:
        print("Player 2 Wins")
        return True
    elif "O" not in diagonal_b and "-" not in diagonal_b:
        print("Player 1 Wins")
        return True
    elif "X" not in diagonal_b and "-" not in diagonal_b:
        print("Player 2 Wins")
        return True
    else:
        return False



def game(board):
    for x in board:
        print(x)
    for turn in range(1,11):
        if check_winner() == True:
            print("We have a winner")
            break
        if turn == 10:
            print("Looks like a stalemate")
        elif turn in player_1_turns:
            player_1_row = "start"
            player_1_column = "start"
            player_1_turn()
        else:

            player_2_row = "start"
            player_2_column = "start"
            player_2_turn()


keep_going = "y"

while keep_going == "y":
    game(board)
    board = make_board()
    keep_going = input("Do you want to play again? Y/n  ").lower()







# def player_1_choice():
#     player_1_row = int(input("Choose a row for an X"))
#     player_1_column = int(input("Choose a column for an X"))

# for x in board:
#     print(x)


# for turn in range(1,11):
#     if check_winner() == True:
#         print("We have a winner")
#         break
#     if turn == 10:
#         print("Looks like a stalemate")
#     elif turn in player_1_turns:
#         player_1_row = "start"
#         player_1_column = "start"
#         player_1_turn()
#     else:
#
#         player_2_row = "start"
#         player_2_column = "start"
#         player_2_turn()


        # print("PLAYER 1 it is your turn \n")
        # while player_1_row not in valid:
        #     player_1_row = int(input("Choose a row for an X:   "))
        # while player_1_column not in valid:
        #     player_1_column = int(input("Choose a column for an X:   "))
        # change_board_1(player_1_row, player_1_column)
        # show_board(board)

    # else:
    #
    #     player_2_row = "start"
    #     player_2_column = "start"
    #     player_2_turn()

        # print("PLAYER 2 it is your turn \n")
        # while player_2_row not in valid:
        #     player_2_row = int(input("Choose a row for an O:   "))
        # while player_2_column not in valid:
        #     player_2_column = int(input("Choose a column for an O:   "))
        #
        # change_board_2(player_2_row, player_2_column)
        # show_board(board)
