import unittest
from algo_work.program_files import find_mwc


class MyTestCase(unittest.TestCase):

    def test_generate_coalitions(self):
        target = 25
        parties = [('A', 2), ('B', 5), ('C', 3), ('D', 4), ('E', 3), ('F', 8)]
        test_sample = find_mwc.generate_coalitions(parties, target)
        self.assertEqual(test_sample, parties)

    def test_minimal_test(self):
        target = 25
        parties = [('A', 2), ('B', 5), ('C', 3), ('D', 4), ('E', 3), ('F', 8)]
        total = 25
        self.assertTrue(find_mwc.minimal_test(parties, total, target))


if __name__ == '__main__':
    unittest.main()
