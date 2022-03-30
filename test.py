import unittest
from adversarial_search import MinMaxWithDepth
from otello_adv_search import *
import numpy as np

class TestMinMaxWithDepth(unittest.TestCase):

    def test_utility(self):
        o = MinMaxWithDepth()
        o.utility = otello_utility
        s0 = np.array([[],[],[]])
        expected_utility = 5
        self.assertEqual(o.utility(s0),expected_utility,f"Should be {expected_utility}")

if __name__ == '__main__':
    unittest.main()

# preguntar heuristicas del futuro