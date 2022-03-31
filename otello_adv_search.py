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
    new_color = -1 if color == 1 else 1
    return new_color

def is_on_board(board,row,column):
    return row < board.shape[0] and row >= 0 and column < board.shape[1] and column >= 0


    
    
    
    



def otello_actions(board:ndarray,rival_color:int):
    actions = []

    rival_positions = np.where(board == rival_color)
    rival_positions = np.array([[row,column] for row, column in zip(rival_positions[0],rival_positions[1])])
    #Up
    up_adjacencies = [[position[0]-1,position[1]] for position in rival_positions if board[position[0]-1,position[1]] == 0]
    own_color = get_oposite_color(rival_color)
    #new_actions = []
    for adj in up_adjacencies:
        
        #action = np.zeros((8,8),dtype=int)

        row = adj[0] + 1
        column = adj[1]
        while board[row,column] != own_color and board[row,column]!=0 and row < board.shape[0]:
            row = row + 1
            #action[row,column] = own_color - board[row,column]
        if board[row,column] == own_color:
            actions.append((adj,[row,column]))
            #new_actions.append(action)
    
    #print(new_actions)
    
    #Down
    down_adjacencies = [[position[0]+1,position[1]] for position in rival_positions if board[position[0]+1,position[1]] == 0]
    for adj in down_adjacencies:
        row = adj[0] - 1 
        column = adj[1]
        while board[row,column] != own_color and board[row,column]!=0 and row >= 0:
            row = row - 1
        if board[row,column] == own_color:
            actions.append((adj,[row,column]))
    
    #Left
    left_adjacencies = [[position[0],position[1]-1] for position in rival_positions if board[position[0],position[1]-1] == 0]
    for adj in left_adjacencies:
        row = adj[0]
        column = adj[1] + 1
        while board[row,column] != own_color and board[row,column]!=0 and column >= 0:
            column = column + 1
        if board[row,column] == own_color:
            actions.append((adj,[row,column]))
    
    #Right
    right_adjacencies = [[position[0],position[1]+1] for position in rival_positions if board[position[0],position[1]+1] == 0]
    for adj in right_adjacencies:
        row = adj[0]
        column = adj[1] - 1
        while board[row,column] != own_color and board[row,column]!=0 and is_on_board(board,row,column):#column < board.shape[1]:
            column = column - 1
        if board[row,column] == own_color:
            actions.append((adj,[row,column]))

    #up_left
    up_left_adjacencies = [[position[0]-1,position[1]-1] for position in rival_positions if board[position[0]-1,position[1]-1] == 0]
    for adj in up_left_adjacencies:
        row = adj[0] + 1
        column = adj[1] +1
        while board[row,column] != own_color and board[row,column]!=0 and is_on_board(board,row,column):
            column = column + 1
            row = row + 1
        if board[row,column] == own_color:
            actions.append((adj,[row,column]))

    #numpy.
    #elemento por elemento con matriz de identidad
    #matriz identidad * parte del tablero.
    #row vs row



    #Right-U
    up_right_adjacencies = [[position[0]-1,position[1]+1] for position in rival_positions if board[position[0]-1,position[1]+1] == 0]
    for adj in up_right_adjacencies:
        row = adj[0] + 1
        column = adj[1] - 1
        while board[row,column] != own_color and board[row,column]!=0 and is_on_board(board,row,column):
            column = column - 1
            row = row + 1
        if board[row,column] == own_color:
            actions.append((adj,[row,column]))
    
    #Left-D
    down_left_adjacencies = [[position[0]+1,position[1]-1] for position in rival_positions if board[position[0]+1,position[1]-1] == 0]
    for adj in down_left_adjacencies:
        row = adj[0] -1
        column = adj[1] + 1
        while board[row,column] != own_color and board[row,column]!=0 and is_on_board(board,row,column):
            column = column + 1
            row = row - 1
        if board[row,column] == own_color:
            actions.append((adj,[row,column]))


    #Right-d
    down_right_adjacencies = [[position[0]+1,position[1]+1] for position in rival_positions if board[position[0]+1,position[1]+1] == 0]
    for adj in down_right_adjacencies:
        row = adj[0] - 1
        column = adj[1] - 1
        while board[row,column] != own_color and board[row,column]!=0 and is_on_board(board,row,column):
            column = column - 1
            row = row - 1
        if board[row,column] == own_color:
            actions.append((adj,[row,column]))

    return actions



def otello_terminal_test(state:ndarray):
    return 5

def otello_heuristic(state:ndarray):
    return 5


def draw_diagonal(next_state,origin,destiny,color):
    o_row = origin[0]
    o_col = origin[1]
    d_row = destiny[0]
    d_col = destiny[1]
    while o_row!=d_row and o_col!=d_col:
        if(o_row<d_row):
            o_row=o_row+1
        if(o_row>d_row):
            o_row=o_row-1
        if(o_col>d_col):
            o_col=o_col-1
        if(o_col<d_col):
            o_col=o_col+1
        next_state[o_row,o_col] = color
    #initial_min_column = min_column
    #while min_row <= max_row:
    #    min_column = initial_min_column
    #    while min_column <= max_column:
    #        next_state[min_row,min_column] = color
    #        min_column = min_column + 1
    #        min_row = min_row + 1

# action = np.array([row,column,color])[]

# color 
# 0 = empty
# 1 = black
# -1 = white


# action = np.array([0,5,1])
def otello_result(state:ndarray, action, color:int):
    next_state = state.copy()
    adjacency = action[0]
    flank_pair = action[1]
    next_state[adjacency[0],adjacency[1]] = color
    adj_row = adjacency[0]
    adj_column = adjacency[1]
    flank_row = flank_pair[0]
    flank_column = flank_pair[1] 
    print("ADJ",adjacency)
    print("FLANK",flank_pair)
    max_row = max(adj_row,flank_row)
    min_row = min(adj_row,flank_row)

    max_column = max(adj_column,flank_column)
    min_column = min(adj_column,flank_column)

    initial_min_column = min_column

    if min_row == max_row or min_column == max_column:
        while min_row <= max_row:
            min_column = initial_min_column
            while min_column <= max_column:
                next_state[min_row,min_column] = color
                min_column = min_column + 1
            min_row = min_row + 1
    else:
        draw_diagonal(next_state,flank_pair,adjacency,color)
        #draw_diagonal(next_state,min_row,max_row, min_column,max_column,color)
    return next_state

def otello_utility(state:ndarray):
    return state.sum()

# initialBoard = np.zeros((8,8),dtype=int)
# initialBoard[3,3] = -1
# initialBoard[4,4] = -1
# initialBoard[4,3] = 1
# initialBoard[3,4] = 1
# print(initialBoard)
# print(otello_actions(initialBoard,-1))
# action = otello_actions(initialBoard,-1)[3]
# print(action)
# s1 = otello_result(initialBoard,action,1)

# print('---------------------------')
# print(s1)
# actions = otello_actions(s1,1)
# print(actions)
# action = actions[1]
# s2 = otello_result(s1,action,-1)
# print(s2)
# print(otello_utility(s2))