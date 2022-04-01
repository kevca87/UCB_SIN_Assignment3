from cProfile import label
from turtle import shape, up
from matplotlib.pyplot import axis
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

# def 
#     row, column = np.where((previous_state == 0)&(current_state != 0))
#     return  

def otello_actions(board:ndarray,color:int):
    actions = []

    rival_color = color * -1

    rival_positions = np.where(board == rival_color)
    rival_positions = np.array([[row,column] for row, column in zip(rival_positions[0],rival_positions[1])])
    #Up
    up_adjacencies = [[position[0]-1,position[1]] for position in rival_positions if is_on_board(board, position[0]-1,position[1]) and board[position[0]-1,position[1]] == 0]
    own_color = color
    
    new_actions = []
    for adj in up_adjacencies:
        
        action = np.zeros((8,8),dtype=int)
        
        row = adj[0]
        column = adj[1]
        action[row,column] = own_color - board[row,column]

        row = adj[0] + 1
        column = adj[1]

        #EQUIVALENT TO THE 2 LINES COMMENTED BELOW, MORE OPTIMAL BASED ON THE NEXT LINK
        #https://stackoverflow.com/a/16244044/18366207 
        flank_limit = np.argmax(board[row:,column]==own_color) + row
        
        # #idx of the own color tiles 
        # own_color_tiles_row_idx = np.where(board[row:,column]==own_color)[0]
        # #if exist a pair tile to flank the rival tiles get the the first row index
        # flank_limit = row + own_color_tiles_row_idx[0] if own_color_tiles_row_idx.shape[0] > 0 else None

        if flank_limit != None:
            #generate the action (addition complement of the current state to get the next state) starting in row 
            action[row:flank_limit,column] = own_color - board[row:flank_limit,column]
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

    result_actions = []
    tiles_added = []
    for action in new_actions:
        row, column = np.where(action**2 == 1)
        tiles_added.append([row[0],column[0]])
    tiles_added = np.unique(tiles_added,axis=0)
    for tile_pos in tiles_added:
        common_movement = list(filter(lambda a: a[tile_pos[0],tile_pos[1]]**2 == 1, new_actions))
        if len(common_movement) >1:
            for action in common_movement[1:]:
                action[tile_pos[0],tile_pos[1]] = 0
        result_action = sum(common_movement)
        result_actions.append(result_action)
             
    return result_actions

def otello_terminal_test(state:ndarray, color):
    return len(otello_actions(state,color))  == 0

def otello_heuristic(state:ndarray):
    return state.sum()

def otello_heuristic_possible_actions(state:ndarray, color: int):
    actions = otello_actions(state,color)
    quantity_of_actions = len(actions) * color
    return quantity_of_actions

def otello_compose_heuristic(state:ndarray, color):
    return state.sum() + otello_heuristic_possible_actions(state, color)
    
# color 
# 0 = empty
# 1 = black
# -1 = white

def otello_result(state:ndarray, action):
    return state + action

def otello_utility(state:ndarray):
    return state.sum()