from turtle import up
import numpy as np
from numpy import ndarray
import copy

import numpy as np

def create_initial_state():
    s0 = np.zeros((8,8),dtype=int)
    s0[3,3] = -1
    s0[4,4] = -1 #WHITE
    s0[4,3] = 1 #BLACK
    s0[3,4] = 1
    return s0

def get_oposite_color(color):
    new_color = -1 if color == 1 else 1
    return new_color

def is_on_board(board,row,column):
    return row < board.shape[0] and row >= 0 and column < board.shape[1] and column >= 0

def otello_actions(board:ndarray,color:int):
    actions = []

    rival_color = color * -1

    rival_positions = np.where(board == rival_color)
    rival_positions = np.array([[row,column] for row, column in zip(rival_positions[0],rival_positions[1])])
    #Up
    up_adjacencies = [[position[0]-1,position[1]] for position in rival_positions if is_on_board(board, position[0]-1,position[1]) and board[position[0]-1,position[1]] == 0]
    own_color = get_oposite_color(rival_color)
    
    new_actions = []
    for adj in up_adjacencies:
        
        action = np.zeros((8,8),dtype=int)
        
        row = adj[0]
        column = adj[1]
        action[row,column] = own_color - board[row,column]
        
        row = adj[0] + 1
        column = adj[1]
        while is_on_board(board,row,column) and board[row,column] != own_color and board[row,column]!=0:
            action[row,column] = own_color - board[row,column]
            row = row + 1
        if is_on_board(board,row,column) and board[row,column] == own_color:
            actions.append((adj,[row,column]))
            new_actions.append(action)
    
    #Down
    down_adjacencies = [[position[0]+1,position[1]] for position in rival_positions if is_on_board(board, position[0]+1,position[1]) and board[position[0]+1,position[1]] == 0]
    for adj in down_adjacencies:
        action = np.zeros((8,8),dtype=int)
        row = adj[0]
        column = adj[1]
        action[row,column] = own_color - board[row,column]
        row = adj[0] - 1 
        column = adj[1]
        while is_on_board(board,row,column) and board[row,column] != own_color and board[row,column]!=0:
            action[row,column] = own_color - board[row,column]
            row = row - 1
        if is_on_board(board,row,column) and  board[row,column] == own_color:
            actions.append((adj,[row,column]))
            new_actions.append(action)
    
    #Left
    left_adjacencies = [[position[0],position[1]-1] for position in rival_positions if is_on_board(board, position[0],position[1]-1) and board[position[0],position[1]-1] == 0]
    for adj in left_adjacencies:
        action = np.zeros((8,8),dtype=int)
        row = adj[0]
        column = adj[1]
        action[row,column] = own_color - board[row,column]
        row = adj[0]
        column = adj[1] + 1
        while is_on_board(board,row,column) and board[row,column] != own_color and board[row,column]!=0:
            action[row,column] = own_color - board[row,column]
            column = column + 1
        if is_on_board(board,row,column) and board[row,column] == own_color:
            actions.append((adj,[row,column]))
            new_actions.append(action)
    
    #Right
    right_adjacencies = [[position[0],position[1]+1] for position in rival_positions if is_on_board(board, position[0],position[1]+1) and  board[position[0],position[1]+1] == 0]
    for adj in right_adjacencies:
        action = np.zeros((8,8),dtype=int)
        row = adj[0]
        column = adj[1]
        action[row,column] = own_color - board[row,column]
        row = adj[0]
        column = adj[1] - 1
        while is_on_board(board,row,column) and board[row,column] != own_color and board[row,column]!=0:#column < board.shape[1]:
            action[row,column] = own_color - board[row,column]
            column = column - 1
        if is_on_board(board,row,column) and board[row,column] == own_color:
            actions.append((adj,[row,column]))
            new_actions.append(action)

    #up_left
    up_left_adjacencies = [[position[0]-1,position[1]-1] for position in rival_positions if is_on_board(board, position[0]-1,position[1]-1) and  board[position[0]-1,position[1]-1] == 0] 
    for adj in up_left_adjacencies:
        action = np.zeros((8,8),dtype=int)
        row = adj[0]
        column = adj[1]
        action[row,column] = own_color - board[row,column]
        row = adj[0] + 1
        column = adj[1] +1
        while is_on_board(board,row,column) and board[row,column] != own_color and board[row,column]!=0:
            action[row,column] = own_color - board[row,column]
            column = column + 1
            row = row + 1
        if is_on_board(board,row,column) and board[row,column] == own_color:
            actions.append((adj,[row,column]))
            new_actions.append(action)

    #numpy.
    #elemento por elemento con matriz de identidad
    #matriz identidad * parte del tablero.
    #row vs row

    #Right-U
    up_right_adjacencies = [[position[0]-1,position[1]+1] for position in rival_positions if is_on_board(board, position[0]-1,position[1]+1) and board[position[0]-1,position[1]+1] == 0]
    for adj in up_right_adjacencies:
        action = np.zeros((8,8),dtype=int)
        row = adj[0]
        column = adj[1]
        action[row,column] = own_color - board[row,column]
        row = adj[0] + 1
        column = adj[1] - 1
        while is_on_board(board,row,column) and board[row,column] != own_color and board[row,column]!=0:
            action[row,column] = own_color - board[row,column]
            column = column - 1
            row = row + 1
        if  is_on_board(board,row,column) and board[row,column] == own_color:
            actions.append((adj,[row,column]))
            new_actions.append(action)
    
    #Left-D
    down_left_adjacencies = [[position[0]+1,position[1]-1] for position in rival_positions if is_on_board(board, position[0]+1,position[1]-1) and board[position[0]+1,position[1]-1] == 0]
    for adj in down_left_adjacencies:
        action = np.zeros((8,8),dtype=int)
        row = adj[0]
        column = adj[1]
        action[row,column] = own_color - board[row,column]
        row = adj[0] -1
        column = adj[1] + 1
        while is_on_board(board,row,column) and board[row,column] != own_color and board[row,column]!=0:
            action[row,column] = own_color - board[row,column]
            column = column + 1
            row = row - 1
        if is_on_board(board,row,column) and board[row,column] == own_color:
            actions.append((adj,[row,column]))
            new_actions.append(action)


    #Right-d
    down_right_adjacencies = [[position[0]+1,position[1]+1] for position in rival_positions if is_on_board(board, position[0]+1,position[1]+1) and board[position[0]+1,position[1]+1] == 0]
    for adj in down_right_adjacencies:
        action = np.zeros((8,8),dtype=int)
        row = adj[0]
        column = adj[1]
        action[row,column] = own_color - board[row,column]
        row = adj[0] - 1
        column = adj[1] - 1
        while is_on_board(board,row,column) and board[row,column] != own_color and board[row,column]!=0:
            action[row,column] = own_color - board[row,column]
            column = column - 1
            row = row - 1
        if is_on_board(board,row,column) and  board[row,column] == own_color:
            actions.append((adj,[row,column]))
            new_actions.append(action)

    return new_actions

def otello_terminal_test(state:ndarray, color):
    return len(otello_actions(state,color))  == 0

def otello_heuristic(state:ndarray):
    return state.sum()

# color 
# 0 = empty
# 1 = black
# -1 = white

def otello_result(state:ndarray, action):
    return state + action

def otello_utility(state:ndarray):
    return state.sum()