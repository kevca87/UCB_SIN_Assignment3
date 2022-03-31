import unittest
from otello_adv_search import *
import numpy as np

class TestOtelloFunctions(unittest.TestCase):

    def test_initial_state(self):
        s0 = create_initial_state()
        utility = otello_utility(s0)
        expected_utility = 0
        self.assertEqual(utility,expected_utility,f'The utility should be {expected_utility}')

    def test_otello_actions(self):
        s0 = create_initial_state()
        actions = otello_actions(s0,-1)
        action = actions[0]
        expected_action = np.zeros((8,8),dtype=int)
        expected_action[2,3] = 1
        expected_action[3,3] = 2
        expected_action[4,3] = 0
        print(action)
        print(expected_action)
        np.testing.assert_array_equal(action,expected_action)
        #self.assertTrue((action == expected_action).all())
        #self.assertEqual(action,expected_action,f'The first action should be {expected_action}')


    def test_otello_result(self):
        s0 = create_initial_state()
        actions = otello_actions(s0,-1)
        action = actions[0]
        s1 = otello_result(s0,action,-1)
        expected_state = np.zeros((8,8),dtype=int)
        
        expected_state[2,3] = 1
        expected_state[3,3] = 1
        expected_state[4,3] = 1
        expected_state[3,4] = 1
        expected_state[4,4] = -1

        print(s1)
        print(expected_state)
        np.testing.assert_array_equal(s1,expected_state)

        #self.assertTrue((s1 == expected_state).all())
        #self.assertEqual(s1,expected_state,f'The next state should be {expectedexpected_state_action}')