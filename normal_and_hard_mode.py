valid = [0,1,2]
player_1_turns = [1,3,5,7,9]
player_2_turns = [2,4,6,8]
keep_going = "y"

def make_board():
    return [["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"]]

def change_board(board, move, player):
    row, column = move
    board[row][column] = player
    return board

def show_board(board):
    for line in board:
        print(line)

def player_move(player):
    player_row = "start"
    player_column = "start"
    while player_row not in valid or player_column not in valid:
        player_row = int(input("Choose a row for an {}:   ".format(player)))
        player_column = int(input("Choose a column for an {}:   ".format(player)))
    return player_row, player_column

def player_turn(player):
    print("PLAYER {} it is your turn \n".format(player))
    move = player_move(player)
    row, column = move
    if board[row][column] == "-":
        change_board(board, move, player)
        show_board(board)
    else:
        print("That spot is taken")
        player_turn(player)

def check_winner():
    column_0 = [board[0][0], board[1][0], board[2][0]]
    column_1 = [board[0][1], board[1][1], board[2][1]]
    column_2 = [board[0][2], board[1][2], board[2][2]]
    diagonal_a = [board[0][0], board[1][1], board[2][2]]
    diagonal_b = [board[0][2], board[1][1], board[2][0]]
    row_0 = board[0]
    row_1 = board[1]
    row_2 = board[2]
    conditions = [column_0, column_1, column_2, diagonal_a, diagonal_b, row_0, row_1, row_2]
    for line in conditions:
        if line == ["X", "X", "X"]:
            print("Player X wins!")
            return True
        elif line == ["O", "O", "O"]:
            print("Player O wins!")
            return True
        else:
            pass

board = make_board()
def game(board):
    for x in board:
        print(x)
    for turn in range(1,11):
        if check_winner() == True:
            break
        if turn == 10:
            print("Looks like a stalemate")
        elif turn in player_1_turns:
            player_turn("X")
        else:
            player_turn("O")

while keep_going == "y":
    game(board)
    board = make_board()
    keep_going = input("Do you want to play again? Y/n  ").lower()
