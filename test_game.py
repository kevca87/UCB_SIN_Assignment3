import unittest
from adversarial_search import MinMaxWithDepth
from otello_adv_search import *
import numpy as np

def to_action(movement):
    column_str = movement[0] 
    row_str = movement[1] 

    row = int(row_str) - 1
    column = ord(column_str) - 65
    return [row,column]
# class TestMinMaxWithDepth(unittest.TestCase):

#     def test_utility(self):
#         o = MinMaxWithDepth()
#         o.utility = otello_utility
#         s0 = np.array([[],[],[]])
#         expected_utility = 5
#         self.assertEqual(o.utility(s0),expected_utility,f"Should be {expected_utility}")
 
class TestGame(unittest.TestCase):

    def test_to_action(self):
        expected_action = [0,0]
        self.assertEqual(to_action('A1'),expected_action,f"Should be {expected_action}")
        
    def test_to_action_B(self):
        expected_action = [3,2]
        self.assertEqual(to_action('C4'),expected_action,f"Should be {expected_action}")

if __name__ == '__main__':
    unittest.main()