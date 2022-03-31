import unittest
from otello_adv_search import *
import numpy as np

class TestOtelloFunctions(unittest.TestCase):

    def test_initial_state(self):
        s0 = create_initial_state()
        utility = otello_utility(s0)
        expected_utility = 0
        self.assertEqual(utility,expected_utility,f'The utility should be {expected_utility}')

    def test_utility(self):
        s0 = np.array([[],[],[]])
        expected_utility = 5
        self.assertEqual(otello_utility(s0),expected_utility,f"Should be {expected_utility}")