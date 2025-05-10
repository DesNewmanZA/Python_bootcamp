# Import needed modules
from game_functions import *

# Define constants
PLAYER_MARKERS = "XO"


def play_game():
    """
    Contains the logic that runs the game by combining use of the other functions
    :return: None
    """
    # Initialize the game
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

    print("Welcome to tic-tac-toe!")
    print("Player 1 will play Xs, player 2 will play Os.")
    print("To place your marker, input the row number and column number e.g. 23. \n")
    print(draw_board(board))

    # Ask for turns for each player until the board is full or there is a winner
    turns = 0
    while turns < 9:
        print("\n")

        # Adjust turn to be specific to the player
        valid_move = False
        while not valid_move:
            choice = input(f"Player {turns % 2 + 1}, please input your selection: ")
            valid_move = check_if_valid_move(board, choice)

        turns += 1
        current_player = turns % 2-1
        take_turn(board, PLAYER_MARKERS[current_player], choice)
        print(draw_board(board))
        # Check if player has won
        game_over, winner = check_if_game_over(board, PLAYER_MARKERS[current_player])
        if game_over:
            break

    # Determine who won
    if winner == "X":
        print("Player 1 wins!")
    elif winner == "O":
        print("Player 2 wins!")
    else:
        print("It's a draw!")


# Run game
if __name__ == "__main__":
    play_game()
