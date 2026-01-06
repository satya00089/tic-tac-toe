"""Tic-Tac-Toe game with AI opponent of varying difficulty levels."""

import math
import random

board = [" " for _ in range(9)]


def print_board():
    """Print the current state of the board."""
    for i in range(0, 9, 3):
        print(board[i], "|", board[i + 1], "|", board[i + 2])
        if i < 6:
            print("--+---+--")


def check_winner(player):
    """Check if the given player has won."""
    wins = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]
    return any(all(board[i] == player for i in combo) for combo in wins)


def is_draw():
    """Check if the game is a draw."""
    return " " not in board


def minimax(is_maximizing):
    """Minimax algorithm to determine the best move score."""
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                best = max(best, minimax(False))
                board[i] = " "
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                best = min(best, minimax(True))
                board[i] = " "
        return best


def random_move():
    """Select a random move from available spots."""
    empty = [i for i in range(9) if board[i] == " "]
    return random.choice(empty)


def best_move():
    """Find the best move for AI using minimax algorithm."""
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move


def ai_move(level):
    """Make a move for the AI based on the difficulty level."""
    if level == "easy":
        move = random_move()
    elif level == "medium":
        move = random_move() if random.random() < 0.5 else best_move()
    else:  # hard
        move = best_move()

    board[move] = "O"


def play_game():
    """Main function to play the game."""
    print("Choose difficulty: easy / medium / hard")
    level = input().lower()

    print("You are X, AI is O")
    print_board()

    while True:
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
            print("Draw!")
            break

        print("AI is thinking...")
        ai_move(level)
        print_board()

        if check_winner("O"):
            print("AI wins!")
            break
        if is_draw():
            print("Draw!")
            break


play_game()
