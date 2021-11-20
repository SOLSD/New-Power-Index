import numpy as np


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
    print(prob_matrix)


set_up_prob_matrix([('A', 2), ('B', 5), ('C', 3), ('D', 4), ('E', 3), ('F', 8)])
