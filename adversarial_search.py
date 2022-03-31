import numpy as np
import copy
from typing import Callable, Any, Iterable

class MinMaxWithDepth:
    def __init__(self):
        self.player = None
        self.actions = None
        self.utility = None
        self.terminal_test = None
        self.result = None

    def arg_max(self,state):
        utilities = []

        own_color = 1 #negras

        for a in self.actions(state,own_color):
            branch_utility = self.min_value(self.result(state,a))
            utilities.append(branch_utility)
        idx = np.argmax(utilities)
        return self.actions(state)[idx]
    
    def arg_min(self,state):
        utilities = []
        for a in self.actions(state):
            branch_utility = self.max_value(self.result(state,a))
            utilities.append(branch_utility)
        idx = np.argmin(utilities)
        return self.actions(state)[idx]
    
    def min_value(self,state):
        if self.terminal_test(state):
            return self.utility(state)
        u = np.inf
        for a in self.actions(state):
            u = min(u,self.max_value(self.result(state,a)))
        return u

    def max_value(self,state):
        if self.terminal_test(state):
            return self.utility(state)
        u = np.inf
        for a in self.actions(state):
            u = min(u,self.min_value(self.result(state,a)))
        return u

    def min_max_decission(self, state):
        if self.player(state) == 'MAX':
            next_action = self.arg_max(state)
        elif self.player(state) == 'MIN':
            next_action = self.arg_min(state)
        return next_action