from os import stat
import pandas as pd
from time import sleep
from turtle import color
import numpy as np
import matplotlib.pyplot as plt
from othello_adv_search import *
from adversarial_search import OthelloMinMaxAlphaBetaWithDepth
import time

def get_initial_state():
    s0 = np.zeros((8,8),dtype=int)
    s0[3,3] = -1
    s0[4,4] = -1 #WHITE
    s0[4,3] = 1 #BLACK
    s0[3,4] = 1
    return s0

def action_to_movement(previous_state, current_state):
    row, column = np.where((previous_state == 0)&(current_state != 0))
    return  chr(column[0] + 65) + str(row[0] +1)

def to_action(movement):
    column_str = movement[0] 
    row_str = movement[1] 

    row = int(row_str) - 1
    column = ord(column_str) - 65
    return [row,column]



print('OTHELLO MASTER')
print('Select your color') 
print('(  1 ) Black')
print('( -1 ) White')
player_color = int(input())
pc1_color = player_color * -1


movement = ''
color = 1


movements = []
times = []
player = []
utilities = []
colors = []


plt.ion()

plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True

fig = plt.figure()
ax = fig.gca()

ax.set_xticks(np.arange(0.5, 8.5, 1))
ax.set_yticks(np.arange(-0.5, -8.5, -1))

ax.set_yticklabels(np.arange(1, 10, 1),minor=True)
ax.set_xticklabels(['A','B','C','D','E','F','G','H'],minor=True)

ax.set_xticks(np.arange(0, 9, 1),minor=True)
ax.set_yticks(np.arange(0, -9, -1),minor=True)

# Gridlines based on minor ticks
ax.grid(which='major', color='grey', linestyle='-', linewidth=1)

movement = ''

#the black tiles always start
color = 1

#data recopilation
movements = []
times = []
player = []
utilities = []
colors = []

#algorithm set
om = OthelloMinMaxAlphaBetaWithDepth()
om.utility = othello_utility
om.actions = othello_actions
om.result = othello_result
om.terminal_test = othello_terminal_test
om.heuristic = othello_heuristic_count_tiles

initial_state = get_initial_state()
state_i = initial_state
depth = 4

while True:
    print(state_i)
    previous_state = state_i.copy()

    #show the board
    blacks = np.where(state_i == 1)
    whites = np.where(state_i == -1)
    empties = np.where(state_i == 0)
    plt.scatter(blacks[1],blacks[0]* -1,color='black',s=500)
    plt.scatter(whites[1],whites[0]* -1,  facecolors='white', edgecolors='black',s=500)
    plt.scatter(empties[1],empties[0]* -1,color='white')
    fig.canvas.draw()
    fig.canvas.flush_events()

    start = time.time()

    if color == pc1_color:
        player.append(f'PC1')
        print('PC1 thinking ...')
        action, expanded_states = om.min_max_cut_off(state_i,pc1_color,depth)

    if color == player_color:
        player.append('P1')
        actions = othello_actions(state_i,color)
        movement = input('P1:')
        movements.append(movement)
        if movement == 'exit':
            break
        movement = to_action(movement)
        
        action = list(filter(lambda a: a[movement[0],movement[1]] != 0, actions))[0]

    print(action)
    end = time.time()
    elapsed_seconds = end - start
    print(f'Time needed {elapsed_seconds}')
    
    if othello_terminal_test(state_i,color):
        utilities.append(othello_utility(state_i))
        movement = 'ND'
        print(f'{color} -> {movement}')
        movements.append(movement)
        my_color = np.where(state_i==color)
        colors.append(len(my_color[0]))
        times.append(elapsed_seconds)
        break
    else:
        state_i = othello_result(state_i,action)
        movement = action_to_movement(previous_state,state_i)
        print(f'{color} -> {movement}')
        movements.append(movement)
        my_color = np.where(state_i==color)
        colors.append(len(my_color[0]))
        times.append(elapsed_seconds)
        u = om.heuristic(state_i,color)
        utilities.append(u)
    

    color = color * -1



try:
    game_details_df = pd.DataFrame({'Player':player,'Movements':movements,'Times':times, 'In-FavorTiles':colors, 'Heuristic':utilities})
    file_name = input('Your file name: ')
    game_details_df.to_csv(f'{file_name}_d{depth}.csv')
except:
    print(file_name)
    print(depth)
    print('player:',len(player))
    print('movements:',len(movements))
    print('times:',len(times))
    print('colors:',len(colors))
    print('heuristics:',len(utilities))