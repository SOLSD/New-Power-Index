import unittest
from algo_work.program_files import find_mwc


class MyTestCase(unittest.TestCase):

    def test_generate_coalitions(self):
        target = 22
        parties = [('A', 2), ('B', 5), ('C', 3), ('D', 4), ('E', 3), ('F', 8)]
        test_sample = find_mwc.generate_coalitions(parties, target)
        expected_result = [[('B', 5), ('C', 3), ('D', 4), ('E', 3), ('F', 8)], [('A', 2), ('B', 5), ('D', 4), ('E', 3), ('F', 8)], [('A', 2), ('B', 5), ('C', 3), ('D', 4), ('F', 8)]]
        self.assertEqual(test_sample, expected_result)

    def test_minimal_test(self):
        target = 25
        parties = [('A', 2), ('B', 5), ('C', 3), ('D', 4), ('E', 3), ('F', 8)]
        total = 25
        self.assertTrue(find_mwc.minimal_test(parties, total, target))


if __name__ == '__main__':
    unittest.main()
