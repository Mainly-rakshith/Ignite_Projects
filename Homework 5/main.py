# Name: Rakshith Jayakarthikeyan
# Assignment: PROG1003 - HW5 - Game

def print_board(board):
    print("+---+---+---+")
    print("| {} | {} | {} |".format(board[0], board[1], board[2]))
    print("+---+---+---+")
    print("| {} | {} | {} |".format(board[3], board[4], board[5]))
    print("+---+---+---+")
    print("| {} | {} | {} |".format(board[6], board[7], board[8]))
    print("+---+---+---+")
    print()

def check_win(board, mark):
    #Rows of board
    if board[0] == mark and board[1] == mark and board[2] == mark:
        return True
    if board[3] == mark and board[4] == mark and board[5] == mark:
        return True
    if board[6] == mark and board[7] == mark and board[8] == mark:
        return True

    #Columns of board
    if board[0] == mark and board[3] == mark and board[6] == mark:
        return True
    if board[1] == mark and board[4] == mark and board[7] == mark:
        return True
    if board[2] == mark and board[5] == mark and board[8] == mark:
        return True

    # diagonals
    if board[0] == mark and board[4] == mark and board[8] == mark:
        return True
    if board[2] == mark and board[4] == mark and board[6] == mark:
        return True

    return False

def full(board):
    for spot in board:
        if spot == " ":
            return False
    return True

def switch_player(player):
    if player == "X":
        return "O"
    else:
        return "X"

def main():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    player = "X"

    while True:
        print("Enter your next move:")

        row = input("Row? (1-3): ")
        if not row.isdigit():
            print("That's not a valid row.")
            continue

        if int(row) < 1 or int(row) > 3:
            print("That's not a valid row.")
            continue

        col = input("Column? (1-3): ")
        if not col.isdigit():
            print("That's not a valid column.")
            continue

        if int(col) < 1 or int(col) > 3:
            print("That's not a valid column.")
            continue

        row_num = int(row) - 1
        col_num = int(col) - 1
        index = row_num * 3 + col_num

        if board[index] != " ":
            print("That spot is already taken.")
            continue

        board[index] = player

        print_board(board)

        if check_win(board, player):
            print("You Win!")
            break

        if full(board):
            print("It's a tie!")
            break

        player = switch_player(player)


if __name__ == "__main__":
    main()