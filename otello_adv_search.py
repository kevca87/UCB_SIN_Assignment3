from turtle import up
import numpy as np
from numpy import ndarray
import copy

import numpy as np

def otello_utility(state:ndarray):
    return 5

def otello_player(state:ndarray):
    return 5

def get_oposite_color(color):
    new_color = 2 if color == 1 else 1
    return new_color

def is_on_board(board,row,column):
    return row < board.shape[0] and row >= 0 and column < board.shape[1] and column >= 0


    
    
    
    
initialBoard = np.zeros((8,8))
initialBoard[3,3] = 2
initialBoard[4,4] = 2
initialBoard[4,3] = 1
initialBoard[3,4] = 1
print(initialBoard)


def otello_actions(board:ndarray,rival_color:int):
    actions = []

    rival_positions = np.where(board == rival_color)
    rival_positions = np.array([[row,column] for row, column in zip(rival_positions[0],rival_positions[1])])
    #Up
    up_adjacencies = [[position[0]-1,position[1]] for position in rival_positions if board[position[0]-1,position[1]] == 0]
    own_color = get_oposite_color(rival_color)
    for adj in up_adjacencies:
        row = adj[0] + 1
        column = adj[1]
        while board[row,column] != own_color and board[row,column]!=0 and row < board.shape[0]:
            row = row + 1
        if board[row,column] == own_color:
            actions.append(adj)
    
    #Down
    down_adjacencies = [[position[0]+1,position[1]] for position in rival_positions if board[position[0]+1,position[1]] == 0]
    for adj in down_adjacencies:
        row = adj[0] - 1 
        column = adj[1]
        while board[row,column] != own_color and board[row,column]!=0 and row >= 0:
            row = row - 1
        if board[row,column] == own_color:
            actions.append(adj)
    
    #Left
    left_adjacencies = [[position[0],position[1]-1] for position in rival_positions if board[position[0],position[1]-1] == 0]
    for adj in left_adjacencies:
        row = adj[0]
        column = adj[1] + 1
        while board[row,column] != own_color and board[row,column]!=0 and column >= 0:
            column = column + 1
        if board[row,column] == own_color:
            actions.append(adj)
    
    #Right
    right_adjacencies = [[position[0],position[1]+1] for position in rival_positions if board[position[0],position[1]+1] == 0]
    for adj in right_adjacencies:
        row = adj[0]
        column = adj[1] - 1
        while board[row,column] != own_color and board[row,column]!=0 and is_on_board(board,row,column):#column < board.shape[1]:
            column = column - 1
        if board[row,column] == own_color:
            actions.append(adj)

    #up_left
    up_left_adjacencies = [[position[0]-1,position[1]-1] for position in rival_positions if board[position[0]-1,position[1]-1] == 0]
    for adj in up_left_adjacencies:
        row = adj[0] + 1
        column = adj[1] +1
        while board[row,column] != own_color and board[row,column]!=0 and is_on_board(board,row,column):
            column = column + 1
            row = row + 1
        if board[row,column] == own_color:
            actions.append(adj)


    #Right-U
    up_right_adjacencies = [[position[0]-1,position[1]+1] for position in rival_positions if board[position[0]-1,position[1]+1] == 0]
    for adj in up_right_adjacencies:
        row = adj[0] + 1
        column = adj[1] - 1
        while board[row,column] != own_color and board[row,column]!=0 and is_on_board(board,row,column):
            column = column - 1
            row = row + 1
        if board[row,column] == own_color:
            actions.append(adj)
    
    #Left-D
    down_left_adjacencies = [[position[0]+1,position[1]-1] for position in rival_positions if board[position[0]+1,position[1]-11] == 0]
    for adj in down_left_adjacencies:
        row = adj[0] -1
        column = adj[1] + 1
        while board[row,column] != own_color and board[row,column]!=0 and is_on_board(board,row,column):
            column = column + 1
            row = row - 1
        if board[row,column] == own_color:
            actions.append(adj)


    #Right-d
    down_right_adjacencies = [[position[0]+1,position[1]+1] for position in rival_positions if board[position[0]+1,position[1]+1] == 0]
    for adj in down_right_adjacencies:
        row = adj[0] - 1
        column = adj[1] - 1
        while board[row,column] != own_color and board[row,column]!=0 and is_on_board(board,row,column):
            column = column - 1
            row = row - 1
        if board[row,column] == own_color:
            actions.append(adj)

    return actions

print(otello_actions(initialBoard,2))

def otello_terminal_test(state:ndarray):
    return 5

def otello_heuristic(state:ndarray):
    return 5

# action = np.array([row,column,color])[]

# color 
# 0 = empty
# 1 = black
# 2 = white


# action = np.array([0,5,1])
def otello_result(state:ndarray, action):
    next_state = state.copy()
    next_state[action[0],action[1]] = action[2]
    
    return next_state