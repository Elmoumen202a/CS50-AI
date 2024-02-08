# Tic-Tac-Toe AI using Minimax

## Project Overview

This project implements an artificial intelligence (AI) to play Tic-Tac-Toe optimally using the Minimax algorithm. The goal is to create a program that, when run, allows a user to play against the AI, ensuring optimal moves are made by both players.

## Project Structure

The project consists of several functions that need to be implemented:

1. **player(board):**
   - Takes a board state as input.
   - Returns which player's turn it is (either X or O).
   - Handles terminal board scenarios.

2. **actions(board):**
   - Returns a set of all possible actions that can be taken on the given board.
   - Each action is represented as a tuple (i, j).
   - Handles terminal board scenarios.

3. **result(board, action):**
   - Takes a board and an action as input.
   - Returns a new board state without modifying the original board.
   - Raises an exception if the action is not valid.
   - Handles terminal board scenarios.

4. **winner(board):**
   - Takes a board as input.
   - Returns the winner of the board (X, O, or None for a tie).
   - Determines the winner based on three-in-a-row horizontally, vertically, or diagonally.
   - Handles terminal board scenarios.

5. **terminal(board):**
   - Takes a board as input.
   - Returns a boolean indicating whether the game is over.
   - Handles scenarios where someone has won or the board is filled without a winner.

6. **utility(board):**
   - Takes a terminal board as input.
   - Outputs the utility of the board (1 for X win, -1 for O win, 0 for a tie).

7. **minimax(board):**
   - Takes a board as input.
   - Returns the optimal move for the player to move on that board using the Minimax algorithm.
   - Returns None if the board is a terminal board.
   - Handles optimal play for both X and O.

## Running the Project

To run the project and play against the AI, use the command:
```bash
python runner.py
