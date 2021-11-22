import numpy as np
import itertools as it


def set_up_prob_matrix(parties):
    """
    Method to create teh matrix of probabilities of parties joining coalitions with others.
    """
    prob_matrix = np.zeros((len(parties), len(parties)))  # Creates an nxn matrix of all 0
    for i in range(len(parties)):
        for j in range(len(parties)):
            if i < j:
                statement = "Enter probability for (", parties[i][0], parties[j][0], ")"
                prob = input(statement)  # User input to give probability to appropriate indices in matrix
                prob_matrix[i][j] = prob
    return prob_matrix


def conductance(parties, mwcs, prob_matrix):
    # everything out over everything out+double everything in
    '''
    for each mwc in mwcs:
        sum probs between parties and double
        sum probs that have one end in mwc
        psi = latter/former+latter
        put psi in list with mwc as tuple
        '''
    # Everything in
    for mwc in mwcs:
        vertices = list(it.combinations(mwc, 2))
        everything_in = 0
        for vertex in vertices:
            row = parties.index(vertex[0])
            column = parties.index(vertex[1])
            everything_in += prob_matrix[row][column]
            print("Vertex:", vertex, "; Row:", row, "; Column:", column, "; To add:", prob_matrix[row][column], "; New everything_in:", everything_in)
    print(prob_matrix)
    print(everything_in)

    # Everything out


prob_matrix = set_up_prob_matrix([('A', 2), ('B', 5), ('C', 3), ('D', 4)])
conductance([('A', 2), ('B', 5), ('C', 3), ('D', 4)], [[('A', 2), ('B', 5), ('C', 3)]], prob_matrix)
