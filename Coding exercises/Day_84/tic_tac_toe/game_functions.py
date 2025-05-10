# Import needed modules
import numpy as np


def draw_board(marker_list):
    """
    Takes a list of played moves and draws a tic-tac-toe board in the terminal

    :param marker_list: a 3 x 3 list matrix of markings of X and O to plot on a tic-tac-toe board

    :return: curr_board: a string that takes has taken the played markings and represented them as a string
    """
    curr_board = ["    1   2   3"]
    for count, row in enumerate(marker_list, start=1):
        curr_board.append(f"{str(count)+"   "+' | '.join(row)}")
        if count != 3:
            curr_board.append("    ---------")
    return "\n".join(curr_board)


def take_turn(curr_board, player_marker, row_col):
    """
    This function takes in the current board state, the current player's marker type and the row and column under
    which they wish to play their turn.

    :param curr_board: a 3 x 3 matrix of the current state of the tic-tac-toe board
    :param player_marker: a string containing "X" or "O" to denote each player
    :param row_col: a string where the first value denotes the row and the second value denotes the column the
                    player wishes to mark
    :return: curr_board: an updated 3 x 3 matrix of the tic-tac-toe board with the latest turn played
    """
    row, col = int(row_col[0])-1, int(row_col[1])-1
    curr_board[row][col] = player_marker
    return curr_board


def check_if_game_over(curr_board, player_marker):
    """
    This function checks the board to see if a player has won by checking for completed rows, columns or diagonals.

    :param curr_board: a 3 x 3 matrix of the current state of the tic-tac-toe board
    :param player_marker: the player for which the board is being checked for a win

    :return: a boolean indicating if the game is won (True) or not and the winning player
    """
    # Check rows
    for row in curr_board:
        if ''.join(row) == player_marker*3:
            return True, player_marker

    # Check columns
    transposed_board = np.array(curr_board).T.tolist()
    for row in transposed_board:
        if ''.join(row) == player_marker*3:
            return True, player_marker

    # Check diagonals
    diagonal_1 = ''.join([curr_board[i][i] for i in range(3)])
    diagonal_2 = ''.join([curr_board[i][2-i] for i in range(3)])
    if diagonal_1 == player_marker*3 or diagonal_2 == player_marker*3:
        return True, player_marker

    return False, None


def check_if_valid_move(curr_board, row_col):
    """
    Checks if the input is valid in the form of rc where r, c is a string of 1, 2, or 3.
    If the input is valid, it is also checked if the move is allowed as the space may be filled on the board already.

    :param curr_board: a 3 x 3 matrix of the current state of the tic-tac-toe board
    :param row_col: a string where the first value denotes the row and the second value denotes the column the
                    player wishes to mark
    :return: a boolean stating whether the move is valid (True) or not.
    """
    if len(row_col) != 2:
        return False
    elif not (1 <= int(row_col[0]) <= 3 and 1 <= int(row_col[1]) <= 3):
        return False
    else:
        row, col = int(row_col[0])-1, int(row_col[1])-1
        if curr_board[row][col] != " ":
            return False
        else:
            return True
