from time import sleep
from turtle import color
import numpy as np
import matplotlib.pyplot as plt
from sympy import block_collapse
from otello_adv_search import *



# fig = plt.figure()
# ax = fig.gca()
# ax.set_xticks(np.arange(0.5, 7.5, 1))
# ax.set_yticks(np.arange(0.5, 7.5, 1))
# plt.grid()
# plt.scatter(blacks[0],blacks[1],color='black',s=500)
# plt.scatter(whites[0],whites[1], color ='beige',s=500)
# plt.scatter(empties[0],empties[1],color='white')
# plt.show()
# sleep(8)
# plt.close(fig)

# x = input()

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 6*np.pi, 100)
y = np.sin(x)

# You probably won't need this if you're embedding things in a tkinter plot...
plt.ion()

# fig = plt.figure()
# ax = fig.add_subplot(111)
# line1, = ax.plot(x, y, 'r-') # Returns a tuple of line objects, thus the comma
# print(line1)

def get_initial_state():
    s0 = np.zeros((8,8),dtype=int)
    s0[3,3] = -1
    s0[4,4] = -1#WHITE
    s0[4,3] = 1#BLACK
    s0[3,4] = 1
    return s0

initial_state = get_initial_state()
state_i = initial_state

fig = plt.figure()
ax = fig.gca()

ax.set_xticklabels(['A','B','C','D','E','F','G','H'])
#ax.set_ytickslabels(np.arange(0, -9, -1),np.arange(1, 10, 1))

ax.set_xticks(np.arange(0, 8, 1),minor=True)
ax.set_yticks(np.arange(0, -8, -1),minor=True)

ax.set_xticks(np.arange(0.5, 8.5, 1))
ax.set_yticks(np.arange(-0.5, -8.5, -1))


plt.grid()



movement = ''
color = 1

def to_action(movement):
    column_str = movement[0] 
    row_str = movement[1] 

    row = int(row_str) - 1
    column = ord(column_str) - 65
    return [row,column]



while movement != 'exit':
    blacks = np.where(state_i == 1)
    whites = np.where(state_i == -1)
    empties = np.where(state_i == 0)
    
    print(blacks[0])
    print(blacks[1])

    plt.scatter(blacks[0],blacks[1]* -1,color='black',s=500)
    plt.scatter(whites[0],whites[1]* -1, color ='beige',s=500)
    plt.scatter(empties[0],empties[1]* -1,color='white')

    fig.canvas.draw()

    movement = input()
    action = to_action(movement)
    print(action)
    
    actions = otello_actions(state_i,color * -1)
    action = list(filter(lambda a: a[0] == action, actions))[0]
    
    state_i = otello_result(state_i,action,color)
    color = color * -1

def draw_map(my_map, path = []):
    #x=16
    xlen = len(my_map[0])
    #y=9
    ylen = len(my_map)
    colormap = colors.ListedColormap(["white","yellow",'lightgreen','red'])

    # set ticks top and bottom
    plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
    plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True

    plt.figure()
    im = plt.imshow(my_map, cmap = colormap)
    ax = plt.gca();

    # Major ticks
    ax.set_xticks(np.arange(0, xlen, 1))
    ax.set_yticks(np.arange(0, ylen, 1))

    # Labels for major ticks
    ax.set_xticklabels(np.arange(0, xlen, 1))
    ax.set_yticklabels(np.arange(0, ylen, 1))

    # Minor ticks
    ax.set_xticks(np.arange(-.5, xlen, 1), minor=True)
    ax.set_yticks(np.arange(-.5, ylen, 1), minor=True)

    # Gridlines based on minor ticks
    ax.grid(which='minor', color='grey', linestyle='-', linewidth=2)

    for step in path:
        plt.plot(step[0], step[1], marker='o', color='b')
        
    ax.text(start[0]-0.2, start[1]+ 0.2, 'S', fontsize=15)
    ax.text(goal[0]-0.2, goal[1]+ 0.2, 'G', fontsize=15)

    plt.show()