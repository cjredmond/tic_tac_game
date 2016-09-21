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
