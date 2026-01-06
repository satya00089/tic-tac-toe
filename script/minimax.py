"""Tic-Tac-Toe game with AI opponent using Minimax algorithm."""

import math

# Create the board
board = [" " for _ in range(9)]


# Print the board
def print_board():
    """Print the current state of the board."""
    for i in range(0, 9, 3):
        print(board[i], "|", board[i + 1], "|", board[i + 2])
        if i < 6:
            print("--+---+--")


# Check winner
def check_winner(player):
    """Check if the given player has won."""
    win_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],  # rows
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],  # columns
        [0, 4, 8],
        [2, 4, 6],  # diagonals
    ]
    return any(all(board[i] == player for i in combo) for combo in win_combinations)


# Check draw
def is_draw():
    """Check if the game is a draw."""
    return " " not in board


# Minimax algorithm
def minimax(is_maximizing):
    """Minimax algorithm to determine the best move score."""
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score


# AI move
def ai_move():
    """Find the best move for AI using minimax algorithm."""
    best_score = -math.inf
    best_move = 0

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = "O"


# Main game loop
def play_game():
    """Main function to play the game."""
    print("Tic Tac Toe")
    print("You are X, AI is O")
    print("Positions are 1-9")

    print_board()

    while True:
        # User move
        move = int(input("Enter your move (1-9): ")) - 1
        if board[move] != " ":
            print("Invalid move!")
            continue
        board[move] = "X"

        print_board()
        if check_winner("X"):
            print("You win!")
            break
        if is_draw():
            print("It's a draw!")
            break

        # AI move
        print("AI is thinking...")
        ai_move()
        print_board()

        if check_winner("O"):
            print("AI wins!")
            break
        if is_draw():
            print("It's a draw!")
            break


play_game()
