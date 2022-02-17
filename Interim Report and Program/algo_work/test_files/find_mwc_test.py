import unittest
from algo_work.program_files import find_mwc


class MyTestCase(unittest.TestCase):

    def test_generate_coalitions(self):
        """
        A test function for generate_coalitions.

        Checks to see if the test sample returns the expected result. In this case the expected result is a list of all
        the MWCs for the given parties and respective target.
        """
        target = 22
        parties = [('A', 2), ('B', 5), ('C', 3), ('D', 4), ('E', 3), ('F', 8)]
        test_sample = find_mwc.generate_coalitions(parties, target)
        expected_result = [[('B', 5), ('C', 3), ('D', 4), ('E', 3), ('F', 8)], [('A', 2), ('B', 5), ('D', 4), ('E', 3),
                                                                                ('F', 8)],
                           [('A', 2), ('B', 5), ('C', 3), ('D', 4), ('F', 8)]]
        self.assertEqual(test_sample, expected_result)

    def test_minimal_test(self):
        """
        A test function for minimal_test.

        Given the target is the sum of the votes in this case, there is only one MWC and that is the grand coalition.
        Hence why the assertTrue function, since only one check needs to be made.
        """
        target = 25
        parties = [('A', 2), ('B', 5), ('C', 3), ('D', 4), ('E', 3), ('F', 8)]
        total = 25
        self.assertTrue(find_mwc.minimal_test(parties, total, target))


if __name__ == '__main__':
    unittest.main()
