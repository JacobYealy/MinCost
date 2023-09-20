import unittest
from a_star import a_star_search
from ida_star import ida_star_search


# =============================================================================
# Algorithm functionality tests
# Jacob Yealy & Caden Rosenberry
#
# Description:
# This class checks the functionality of the A* and IDA* algorithms.
# The first test checks that the minimum cost is found by the algorithms.
# The second test checks that the algorithm determines if no path exists.
# =============================================================================
class TestAStar(unittest.TestCase):

    def test_case_1(self):
        # Tests that the minimum path is taken when possible
        graph = {
            1: {2: 2, 3: 4},
            2: {4: 7},
            3: {2: 1, 4: 5},
            4: {}
        }
        h_costs = {1: 0, 2: 1, 3: 3, 4: 0}
        start, end = 1, 4

        cost, path = a_star_search(graph, h_costs, start, end)

        self.assertEqual(cost, 10)
        self.assertEqual(path, [1, 2, 4])

    def test_case_no_path(self):
        # Tests the functionality of no existing path
        graph = {1: {}, 2: {}}
        h_costs = {1: 0, 2: 0}
        start, end = 1, 2

        cost, path = a_star_search(graph, h_costs, start, end)

        self.assertIsNone(cost)
        self.assertIsNone(path)


class TestIDAStar(unittest.TestCase):

    def test_case_1(self):
        # Tests that the minimum path is taken when possible
        graph = {
            1: {2: 2, 3: 4},
            2: {4: 7},
            3: {2: 1, 4: 5},
            4: {}
        }
        h_costs = {1: 0, 2: 1, 3: 3, 4: 0}
        start, end = 1, 4

        cost, path = ida_star_search(graph, h_costs, start, end)

        self.assertEqual(cost, 9)
        self.assertEqual(path, [1, 2, 4])

    def test_case_no_path(self):
        # Tests no possible path
        graph = {1: {}, 2: {}}
        h_costs = {1: 0, 2: 0}
        start, end = 1, 2

        cost, path = ida_star_search(graph, h_costs, start, end)

        self.assertIsNone(cost)
        self.assertIsNone(path)

if __name__ == '__main__':
    unittest.main()