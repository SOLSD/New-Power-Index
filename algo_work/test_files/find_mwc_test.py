import unittest
from algo_work.program_files import find_mwc


class MyTestCase(unittest.TestCase):

    def test_generate_coalitions(self):
        target = 23
        parties = [('A', 2), ('B', 5), ('C', 3), ('D', 4), ('E', 3), ('F', 8)]
        test_sample = find_mwc.generate_coalitions(parties, target)
        self.assertEqual(test_sample, parties)  # add assertion here


if __name__ == '__main__':
    unittest.main()
