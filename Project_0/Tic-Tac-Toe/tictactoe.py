"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    X_count = 0
    O_count = 0
    
    # Count  X and O 
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == X:
                X_count += 1
            if board[row][column] == O:
                O_count += 1

    if X_count > O_count:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    """
    Each action should be represented as a tuple (i, j) 
    where i corresponds to the row of the move (0, 1, or 2) 
    and j corresponds to which cell in the row corresponds 
    to the move (also 0, 1, or 2).
    """
    possibilities = set()

    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == EMPTY:
                possibilities.add((row,column))

    return possibilities


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception('Action is not a valid action for the board!')

    boardCopy = copy.deepcopy(board)
    row, column= action
    boardCopy[row][column] = player(board)
    return boardCopy

#  win the game with 3  in a row hor.
def check_rows(board,player):
    for row in range(len(board)):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    return False

# win the game with 3 in a row vert.
def check_columns(board,player):
    for column in range(len(board)):
        if board[0][column] == player and board[1][column] == player and board[2][column] == player:
            return True
    return False

# win the game with 3  in a row diag.
def ccheckBottomTop_dig(board,player):
    count = 0
    for row in range(len(board)):
        for column in range(len(board[row])):
            # I need to change this part
            if row == column and board[row][len(board) - row - 1] == player:
                count += 1
    return count == 3

# win the game with 3  in a row diag.
def checkTopBottom_dig(board,player):
    count = 0
    for row in range(len(board)):
        for column in range(len(board[row])):
            if row == column and board[row][column] == player:
                count += 1
    return count == 3    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # X player has won the game, return X. 
    if check_rows(board,X) or check_columns(board,X) or checkTopBottom_dig(board,X) or ccheckBottomTop_dig(board,X):
        return X  
    # O player has won the game, return O.
    elif check_rows(board,O) or check_columns(board,O) or checkTopBottom_dig(board,O) or ccheckBottomTop_dig(board,O):
        return O
    #  no winner of the game , return None.
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X:
        return True
    if winner(board) == O:
        return True 
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    You may assume utility will only be called on a board if terminal(board) is True
    """
    # If X has won the game,1. 
    if winner(board) == X:
        return 1
    # If O has won the game,-1. 
    elif winner(board) == O:
        return -1
    # If the game has ended ,0.
    else:
        return 0

def maxValue(board):
    v = -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, minValue(result(board, action)))
    return v

def minValue(board):
    v = math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, maxValue(result(board, action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    The move returned should be the optimal action (i, j) that is one of the allowable actions on the board. 
    If multiple moves are equally optimal, any of those moves is acceptable.
    """
    if terminal(board):
        return None
    # Case of player is X
    elif player(board) == X:
        plays = []
        for action in actions(board):
            #  minValue and the action that results to its value
            plays.append([minValue(result(board,action)), action])
        # Reverse 
        return sorted(plays, key=lambda rev: rev[0], reverse=True)[0][1] 
    # Case of player is O
    elif player(board) == O:
        plays = []
        for action in actions(board):
            #  maxValue and the action that results to its value
            plays.append([maxValue(result(board,action)), action])
        # Reverse
        return sorted(plays, key=lambda x: x[0])[0][1]