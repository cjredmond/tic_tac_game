board = [["-", "-", "-"],
         ["-", "-", "-"],
         ["-", "-", "-"]
         ]
valid = [0,1,2]
player_1_turns = [1,3,5,7,9]
player_2_turns = [2,4,6,8]

def make_board():
    return [["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"]
             ]

def change_board(board, row, column, player):
    board[row][column] = player
    return board

def show_board(board):
    for line in board:
        print(line)

def player_choice_column(player):
    player_column = "start"
    while player_column not in valid:
        player_column = int(input("Choose a column for an {}:   ".format(player)))
    return player_column

def player_choice_row(player):
    player_row = "start"
    while player_row not in valid:
        player_row = int(input("Choose a row for an {}:   ".format(player)))
    return player_row

def player_move(player):
    player_row = "start"
    player_column = "start"
    while player_row not in valid or player_column not in valid:
        player_row = int(input("Choose a row for an {}:   ".format(player)))
        player_column = int(input("Choose a column for an {}:   ".format(player)))
    return player_row, player_column




def player_1_turn():
    print("PLAYER 1 it is your turn \n")
    row = player_choice_row("X")
    column = player_choice_column("X")
    if board[row][column] == "-":
        change_board(board, row, column,  "X")
        show_board(board)
    else:
        print("That spot is taken")
        player_1_turn()

def player_2_turn():
    print("PLAYER 2 it is your turn \n")
    row = player_choice_row("O")
    column = player_choice_column("O")
    if board[row][column] == "-":
        change_board(board, row, column, "O")
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
            player_1_turn()
        else:
            player_2_turn()

keep_going = "y"

while keep_going == "y":
    game(board)
    board = make_board()
    keep_going = input("Do you want to play again? Y/n  ").lower()
