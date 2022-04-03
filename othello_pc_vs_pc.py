from os import stat
import pandas as pd
from time import sleep
from turtle import color
import numpy as np
import matplotlib.pyplot as plt
from adversarial_search import OthelloMinMaxAlphaBetaWithDepth
#from adversarial_search import OthelloMinMaxWithDepth
import time

from othello_adv_search import *

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

print('OTHELLO MASTER PC vs. PC')

heuristics = {
    #'possible actions':othello_heuristic_possible_actions,
    'count tiles sum':othello_heuristic_count_tiles,
    #'count tiles sum + possible actions':othello_heuristic_count_tiles
}


#depth = 3
depth = 4
#depth = 5



def game(heuristic,depth):
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

    #pc1 will play the black tiles (first turn)
    pc1_color = 1
    #pc2 will play the white tiles (second turn)
    pc2_color = -1

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
    #om = OthelloMinMaxWithDepth()
    om.utility = othello_utility
    om.actions = othello_actions
    om.result = othello_result
    om.terminal_test = othello_terminal_test
    om.heuristic = heuristic

    initial_state = get_initial_state()
    state_i = initial_state
    n_actions_expanded = []

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
            action, actions_expanded = om.min_max_cut_off(state_i,pc1_color,depth)

        if color == pc2_color:
            player.append(f'PC2')
            print('PC2 thinking ...')
            action, actions_expanded = om.min_max_cut_off(state_i,pc2_color,depth)

        end = time.time()
        elapsed_seconds = end - start
        n_actions_expanded.append(actions_expanded)
        print('Actions expanded: ',actions_expanded)
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
        game_details_df = pd.DataFrame({'Player':player,'Movements':movements,'Times':times, 'In-FavorTiles':colors, 'Heuristic':utilities, 'Actions expanded':n_actions_expanded})
        file_name = input('Your file name: ')
        game_details_df.to_csv(f'{file_name}_d{depth}.csv')
    except:
        print(file_name)
        print(heuristic)
        print(depth)
        print('player:',len(player))
        print('movements:',len(movements))
        print('times:',len(times))
        print('colors:',len(colors))
        print('heuristics:',len(utilities))

for heuristic in heuristics:
    print(heuristic)
    game(heuristics[heuristic],depth)