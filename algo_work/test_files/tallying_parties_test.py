import unittest
from algo_work.program_files import tallying_parties


class MyTestCase(unittest.TestCase):

    def test_tally(self):
        mwcs = [[('a', 6), ('d', 5)], [('a', 6), ('e', 4)], [('a', 6), ('g', 6)], [('d', 5), ('g', 6)]]
        test_sample = tallying_parties.tally(mwcs)
        expected_result = [('a', 0.375), ('d', 0.25), ('e', 0.125), ('g', 0.25)]
        self.assertEqual(test_sample, expected_result)


if __name__ == '__main__':
    unittest.main()
