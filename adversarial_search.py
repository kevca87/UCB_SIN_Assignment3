import numpy as np
import copy
from typing import Callable, Any, Iterable
from otello_adv_search import *

class OtelloMinMaxWithDepth:
    def __init__(self):
        self.player = None
        self.actions = None
        self.utility = None
        self.terminal_test = None
        self.result = None
        self.heuristic = None

    def cut_off(self,depth):
        return depth == 0
    

    def arg_max(self,state,depth):
        utilities = []
        color = 1
        actions = self.actions(state,color)
        for a in actions:
            branch_utility = self.min_value(self.result(state,a),depth)
            utilities.append(branch_utility)
        idx = np.argmax(utilities)
        return actions[idx]
    
    def arg_min(self,state,depth):
        utilities = []
        color = -1
        actions = self.actions(state,color)
        for a in actions:
            branch_utility = self.max_value(self.result(state,a),depth)
            utilities.append(branch_utility)
        idx = np.argmin(utilities)
        return actions[idx]
    
    def min_value(self,state,depth,alpha=-np.inf,beta=np.inf):
        color = -1
        if self.cut_off(depth):
            return self.heuristic(state)
        if self.terminal_test(state,color):
            return self.utility(state)
        u = np.inf
        actions = self.actions(state,color)
        for a in actions:
            u = min(u,self.max_value(self.result(state,a),depth-1,alpha,beta))
            if u <= alpha:
                return u
            beta = min(beta,u)
        return u

    def max_value(self,state,depth,alpha=-np.inf,beta=np.inf):
        color = 1
        if self.cut_off(depth):
            return self.heuristic(state)
        if self.terminal_test(state,color):
            return self.utility(state)
        u = - np.inf
        actions = self.actions(state,color)
        for a in actions:
            u = max(u,self.min_value(self.result(state,a),depth-1,alpha,beta))
            if u >= beta:
                return u
            alpha = max(alpha,u)
        return u

    #color is the color of the player that the machine represents
    def min_max_cut_off(self, state: np.ndarray, color: int,depth):
        if color == 1: #blacks
            next_action = self.arg_max(state,depth)
        elif color == -1: #whites
            next_action = self.arg_min(state,depth)
        return next_action


