board = [["-", "-", "-"],
         ["-", "-", "-"],
         ["-", "-", "-"]
         ]
valid = [0,1,2]
player_1_turns = [1,3,5,7,9]
player_2_turns = [2,4,6,8]


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
    change_board_1(row, column)
    show_board(board)
def player_2_turn():
    print("PLAYER 2 it is your turn \n")
    row = player_2_choice_row()
    column = player_2_choice_column()
    change_board_2(row, column)
    show_board(board)

def check_winner():
    if "X" and "-" not in board[0]:
        return True
    elif "O" and "-" not in board[0]:
        return True
    elif "X" and "-" not in board[1]:
        return True
    elif "O" and "-" not in board[1]:
        return True
    elif "X" and "-" not in board[2]:
        return True
    elif "O" and "-" not in board[2]:
        return True






# def player_1_choice():
#     player_1_row = int(input("Choose a row for an X"))
#     player_1_column = int(input("Choose a column for an X"))

for x in board:
    print(x)


for turn in range(1,10):
    if check_winner() == True:
        print("We have a winner")
        break
    elif turn in player_1_turns:
        player_1_row = "start"
        player_1_column = "start"
        player_1_turn()


        # print("PLAYER 1 it is your turn \n")
        # while player_1_row not in valid:
        #     player_1_row = int(input("Choose a row for an X:   "))
        # while player_1_column not in valid:
        #     player_1_column = int(input("Choose a column for an X:   "))
        # change_board_1(player_1_row, player_1_column)
        # show_board(board)

    else:

        player_2_row = "start"
        player_2_column = "start"
        player_2_turn()

        # print("PLAYER 2 it is your turn \n")
        # while player_2_row not in valid:
        #     player_2_row = int(input("Choose a row for an O:   "))
        # while player_2_column not in valid:
        #     player_2_column = int(input("Choose a column for an O:   "))
        #
        # change_board_2(player_2_row, player_2_column)
        # show_board(board)
