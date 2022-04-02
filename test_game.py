import unittest
from adversarial_search import OtelloMinMaxAlphaBetaWithDepth
from otello_adv_search import *
import numpy as np

def to_action(movement):
    column_str = movement[0] 
    row_str = movement[1] 

    row = int(row_str) - 1
    column = ord(column_str) - 65
    return [row,column]
 
class TestGame(unittest.TestCase):

    def test_to_action(self):
        expected_action = [0,0]
        self.assertEqual(to_action('A1'),expected_action,f"Should be {expected_action}")
        
    def test_to_action_B(self):
        expected_action = [3,2]
        self.assertEqual(to_action('C4'),expected_action,f"Should be {expected_action}")

if __name__ == '__main__':
    unittest.main()