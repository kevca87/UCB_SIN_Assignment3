import numpy as np
import copy
from typing import Callable, Any, Iterable
from othello_adv_search import *

class OthelloMinMaxAlphaBetaWithDepth:
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
        total_actions_expanded = 0
        for a in actions: 
            branch_utility, actions_expanded = self.min_value(self.result(state,a),depth)
            total_actions_expanded = total_actions_expanded + actions_expanded
            utilities.append(branch_utility)
        best_action = None
        if len(utilities) > 0:
            idx = np.argmax(utilities)
            best_action = actions[idx]
        return best_action, total_actions_expanded
    
    def arg_min(self,state,depth):
        utilities = []
        color = -1
        actions = self.actions(state,color)
        total_actions_expanded = 0
        for a in actions:
            branch_utility, actions_expanded = self.max_value(self.result(state,a),depth)
            total_actions_expanded = total_actions_expanded + actions_expanded
            utilities.append(branch_utility)
        best_action = None
        if len(utilities) > 0:
            idx = np.argmin(utilities)
            best_action = actions[idx]
        return best_action, total_actions_expanded
    
    #add if terminal test before for a in actions to avoid game over error. arg min and arg max



    def min_value(self,state,depth,alpha=-np.inf,beta=np.inf,actions_expanded=0):
        color = -1
        if self.terminal_test(state,color):
            return self.utility(state), actions_expanded
        if self.cut_off(depth):
            return self.heuristic(state,color), actions_expanded
        u = np.inf
        actions = self.actions(state,color)
        for a in actions:
            actions_expanded = actions_expanded + 1
            max_u, actions_expanded = self.max_value(self.result(state,a),depth-1,alpha,beta,actions_expanded)
            u = min(u,max_u)
            if u <= alpha:
                return u ,actions_expanded
            beta = min(beta,u)
        return u, actions_expanded

    def max_value(self,state,depth,alpha=-np.inf,beta=np.inf,actions_expanded=0):
        color = 1
        if self.terminal_test(state,color):
            return self.utility(state), actions_expanded
        if self.cut_off(depth):
            return self.heuristic(state,color), actions_expanded
        u = - np.inf
        actions = self.actions(state,color)
        for a in actions:
            actions_expanded = actions_expanded + 1
            min_u, actions_expanded = self.min_value(self.result(state,a),depth-1,alpha,beta,actions_expanded)
            u = max(u,min_u)
            if u >= beta:
                return u, actions_expanded
            alpha = max(alpha,u)
        return u, actions_expanded

    #color is the color of the player that the machine represents
    def min_max_cut_off(self, state: np.ndarray, color: int,depth):
        if color == 1: #blacks
            next_action, actions_expanded = self.arg_max(state,depth)
        elif color == -1: #whites
            next_action, actions_expanded = self.arg_min(state,depth)
        return next_action, actions_expanded



class OthelloMinMaxWithDepth:
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
        total_actions_expanded = 0
        for a in actions: 
            branch_utility, actions_expanded = self.min_value(self.result(state,a),depth)
            total_actions_expanded = total_actions_expanded + actions_expanded
            utilities.append(branch_utility)
        best_action = None
        if len(utilities) > 0:
            idx = np.argmax(utilities)
            best_action = actions[idx]
        return best_action, total_actions_expanded
    
    def arg_min(self,state,depth):
        utilities = []
        color = -1
        actions = self.actions(state,color)
        total_actions_expanded = 0
        for a in actions:
            branch_utility, actions_expanded = self.max_value(self.result(state,a),depth)
            total_actions_expanded = total_actions_expanded + actions_expanded
            utilities.append(branch_utility)
        best_action = None
        if len(utilities) > 0:
            idx = np.argmin(utilities)
            best_action = actions[idx]
        return best_action, total_actions_expanded
    
    #add if terminal test before for a in actions to avoid game over error. arg min and arg max



    def min_value(self,state,depth,actions_expanded=0):
        color = -1
        if self.terminal_test(state,color):
            return self.utility(state), actions_expanded
        if self.cut_off(depth):
            return self.heuristic(state,color), actions_expanded
        u = np.inf
        actions = self.actions(state,color)
        for a in actions:
            actions_expanded = actions_expanded + 1
            max_u, actions_expanded = self.max_value(self.result(state,a),depth-1,actions_expanded)
            u = min(u,max_u)
        return u, actions_expanded

    def max_value(self,state,depth,actions_expanded=0):
        color = 1
        if self.terminal_test(state,color):
            return self.utility(state), actions_expanded
        if self.cut_off(depth):
            return self.heuristic(state,color), actions_expanded
        u = - np.inf
        actions = self.actions(state,color)
        for a in actions:
            actions_expanded = actions_expanded + 1
            min_u, actions_expanded = self.min_value(self.result(state,a),depth-1,actions_expanded)
            u = max(u,min_u)
        return u, actions_expanded

    #color is the color of the player that the machine represents
    def min_max_cut_off(self, state: np.ndarray, color: int,depth):
        if color == 1: #blacks
            next_action, actions_expanded = self.arg_max(state,depth)
        elif color == -1: #whites
            next_action, actions_expanded = self.arg_min(state,depth)
        return next_action, actions_expanded
