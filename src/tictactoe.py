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
    xCount = 0
    oCount = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                xCount += 1
            elif board[i][j] == O:
                oCount += 1
    
    if xCount == oCount:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleActions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                possibleActions.add((i,j))
    
    return possibleActions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    x,y = action

    if x > 2 or x < 0 or y > 2 or y < 0:
        raise ValueError("Action value out of range")
    
    playerName = player(board)
    newBoard = copy.deepcopy(board)
    newBoard[x][y] = playerName

    return newBoard


def winner(board):
    """
    Returns the winner of the game (X or O), if there is one.
    Otherwise returns None.
    """
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != None:
            return board[i][0]
    
    # Check columns  
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != None:
            return board[0][j]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != None:
        return board[0][2]
    
    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    winnerValue = winner(board)

    if winnerValue is not None:
        return True
    
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                return False

    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
    winnerValue = winner(board)

    if winnerValue == X:
        return 1
    elif winnerValue == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    current_player = player(board)
    
    if current_player == X:
        _, best_move = get_best_move(board, True, -math.inf, math.inf)
    else:
        _, best_move = get_best_move(board, False, -math.inf, math.inf)
    
    return best_move


def get_best_move(board, is_maximizing, alpha, beta):
    """
    One simple function that handles both X and O
    """
    # Game over? Return the score
    if terminal(board):
        return utility(board), None
    
    if is_maximizing:  # X's turn - wants HIGH score
        best_score = -math.inf
        best_move = None
        
        for move in actions(board):
            new_board = result(board, move)
            score, _ = get_best_move(new_board, False, alpha, beta)
            
            if score > best_score:
                best_score = score
                best_move = move
            
            alpha = max(alpha, score)
            if beta <= alpha:
                break  # PRUNE/CUT ! Stop looking at other moves
        
        return best_score, best_move
    
    else:  # O's turn - wants LOW score  
        best_score = math.inf
        best_move = None
        
        for move in actions(board):
            new_board = result(board, move)
            score, _ = get_best_move(new_board, True, alpha, beta)
            
            if score < best_score:
                best_score = score
                best_move = move
            
            beta = min(beta, score)
            if beta <= alpha:
                break  # PRUNE/CUT ! Stop looking at other moves
        
        return best_score, best_move