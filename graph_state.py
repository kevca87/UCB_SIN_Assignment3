from time import sleep
from turtle import color
import numpy as np
import matplotlib.pyplot as plt
from otello_adv_search import *

x = np.linspace(0, 6*np.pi, 100)
y = np.sin(x)

plt.ion()

def get_initial_state():
    s0 = np.zeros((8,8),dtype=int)
    s0[3,3] = -1
    s0[4,4] = -1 #WHITE
    s0[4,3] = 1 #BLACK
    s0[3,4] = 1
    return s0

initial_state = get_initial_state()
state_i = initial_state

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
color = 1

def to_action(movement):
    column_str = movement[0] 
    row_str = movement[1] 

    row = int(row_str) - 1
    column = ord(column_str) - 65
    return [row,column]



while movement != 'exit':
    print(state_i)
    blacks = np.where(state_i == 1)
    whites = np.where(state_i == -1)
    empties = np.where(state_i == 0)
    #print('whites:',whites)
    
    plt.scatter(blacks[1],blacks[0]* -1,color='black',s=500)
    plt.scatter(whites[1],whites[0]* -1,  facecolors='white', edgecolors='black',s=500)
    plt.scatter(empties[1],empties[0]* -1,color='white')

    fig.canvas.draw()

    movement = input()
    if movement == 'exit':
        break

    movement = to_action(movement)
    #print(action)
    
    actions = otello_actions(state_i,color)
    #print(actions)

    actions = list(filter(lambda a: a[movement[0],movement[1]] != 0, actions))

    if len(actions) > 1:
        for a in actions[1:]:
            a[movement[0],movement[1]] = 0
    
    for action in actions:
        #that allow draw eatings in differents directions at the same time.
        #message 31/03 10:56
        state_i = otello_result(state_i,action)
    color = color * -1