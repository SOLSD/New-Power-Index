import unittest
from algo_work.program_files import find_mwc, graph_theory_section


class MyTestCase(unittest.TestCase):
    def test_set_up_prob_matrix(self):

        parties = [('A', 2), ('B', 5), ('C', 3), ('D', 4), ('E', 3), ('F', 8)]
        prob_matrix = graph_theory_section.set_up_prob_matrix(parties)

        for i in range(len(parties)):
            for j in range(len(parties)):
                self.assertEqual(prob_matrix[i][j], prob_matrix[j][i])

    def test_conductance(self):
        """
        Test designed to input numbers sequentially 1 - 9 and repeat until matrix is full
        """
        parties = [('A', 2), ('B', 5), ('C', 3), ('D', 4), ('E', 3), ('F', 8)]
        mwcs = find_mwc.generate_coalitions(parties, 18)
        prob_matrix = graph_theory_section.set_up_prob_matrix(parties)
        conductances = graph_theory_section.conductance(parties, mwcs, prob_matrix)
        self.assertEqual(conductances, [([('C', 3), ('D', 4), ('E', 3), ('F', 8)], 0.5116279069767442),
                                        ([('B', 5), ('D', 4), ('E', 3), ('F', 8)], 0.24271844660194175),
                                        ([('B', 5), ('C', 3), ('E', 3), ('F', 8)], 0.29896907216494845),
                                        ([('B', 5), ('C', 3), ('D', 4), ('F', 8)], 0.3333333333333333),
                                        ([('A', 2), ('B', 5), ('E', 3), ('F', 8)], 0.32653061224489793),
                                        ([('A', 2), ('B', 5), ('D', 4), ('F', 8)], 0.3617021276595745),
                                        ([('A', 2), ('B', 5), ('C', 3), ('F', 8)], 0.4090909090909091)])

    def test_cep(self):
        """
        Test designed to input numbers sequentially 1 - 9 and repeat until matrix is full
        """
        parties = [('A', 2), ('B', 5), ('C', 3), ('D', 4), ('E', 3), ('F', 8)]
        mwcs = find_mwc.generate_coalitions(parties, 18)
        prob_matrix = graph_theory_section.set_up_prob_matrix(parties)
        ceps = graph_theory_section.cep(parties, mwcs, prob_matrix)
        self.assertEqual(ceps, [([('C', 3), ('D', 4), ('E', 3), ('F', 8)], 720.0),
                                ([('B', 5), ('D', 4), ('E', 3), ('F', 8)], 60480.0),
                                ([('B', 5), ('C', 3), ('E', 3), ('F', 8)], 15552.0),
                                ([('B', 5), ('C', 3), ('D', 4), ('F', 8)], 5670.0),
                                ([('A', 2), ('B', 5), ('E', 3), ('F', 8)], 8640.0),
                                ([('A', 2), ('B', 5), ('D', 4), ('F', 8)], 4725.0),
                                ([('A', 2), ('B', 5), ('C', 3), ('F', 8)], 1620.0)])


if __name__ == '__main__':
    unittest.main()
