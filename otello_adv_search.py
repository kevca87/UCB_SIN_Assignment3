import numpy as np
from numpy import ndarray
import copy

import numpy as np

def otello_utility(state:ndarray):
    return 5

def otello_player(state:ndarray):
    return 5

def get_adjacents(board:ndarray,adjacent_color:int):
    rival_positions = np.where(board == adjacent_color)
    rival_positions = np.array([[row,column] for row, column in zip(rival_positions[0],rival_positions[1])])
    #Up
    up_adjacencies = [[position[0]-1,position[1]] for position in rival_positions if board[position[0]-1,position[1]] == 0]
    #Down
    down_adjacencies = [[position[0]+1,position[1]] for position in rival_positions if board[position[0]+1,position[1]] == 0]
    #Left
    left_adjacencies = [[position[0],position[1]-1] for position in rival_positions if board[position[0],position[1]-1] == 0]
    #Right
    right_adjacencies = [[position[0],position[1]+1] for position in rival_positions if board[position[0],position[1]+1] == 0]
    # print('up:',up_adjacencies)
    # print('down:',down_adjacencies)
    # print('left:',left_adjacencies)
    # print('right:',right_adjacencies)
    #up_left
    up_left_adjacencies = [[position[0]-1,position[1]-1] for position in rival_positions if board[position[0]-1,position[1]-1] == 0]
    #Right-U
    up_right_adjacencies = [[position[0]-1,position[1]+1] for position in rival_positions if board[position[0]-1,position[1]+1] == 0]
    #Left-D
    down_left_adjacencies = [[position[0]+1,position[1]-1] for position in rival_positions if board[position[0]+1,position[1]-11] == 0]
    #Right-d
    down_right_adjacencies = [[position[0]+1,position[1]+1] for position in rival_positions if board[position[0]+1,position[1]+1] == 0]
    # print('up_left:',up_left_adjacencies)
    # print('up_right:',up_right_adjacencies)
    # print('down-left:',down_left_adjacencies)
    # print('down-right:',down_right_adjacencies)
    adjacencies = np.unique(up_adjacencies+down_adjacencies+left_adjacencies+right_adjacencies+up_left_adjacencies+up_right_adjacencies+down_left_adjacencies+down_right_adjacencies,axis=0)
    return adjacencies
    
    
    
    
initialBoard = np.zeros((8,8))
initialBoard[3,3] = 2
initialBoard[4,4] = 2
initialBoard[4,3] = 1
initialBoard[3,4] = 1
print(initialBoard)


print(get_adjacents(initialBoard,2))

def otello_actions(state:ndarray):
    victim = 2
    adjacencies = get_adjacents(state,victim)
    
    return 5

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