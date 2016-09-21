board = [["-", "-", "-"],
         ["-", "-", "-"],
         ["-", "-", "-"]
         ]
valid = [0,1,2]
def player_move(player):
    player_row = "start"
    player_column = "start"
    while player_row not in valid or player_column not in valid:
        player_row = int(input("Choose a row for an {}:   ".format(player)))
        player_column = int(input("Choose a column for an {}:   ".format(player)))
    return player_row, player_column

move = player_move("X")



def change_board(board, move, player):
    row, column = move
    board[row][column] = player
    return board
change_board(board, move, "X")

print(board)

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
