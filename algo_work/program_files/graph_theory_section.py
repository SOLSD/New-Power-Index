import numpy as np
import itertools as it


def set_up_prob_matrix(parties, prob_location):
    """
    Method to create the matrix of probabilities of parties joining coalitions with others.
    """
    fileobj = open(prob_location)
    prob_data = fileobj.readlines()
    prob_data = [line.strip() for line in prob_data]
             
    prob_index = 0
                
    prob_matrix = np.zeros((len(parties), len(parties)))  # Creates an nxn matrix of all 0
    for i in range(len(parties)):
        for j in range(len(parties)):
            if i < j:
                prob_matrix[i][j] = float(prob_data[prob_index])
                prob_matrix[j][i] = float(prob_data[prob_index])
                prob_index += 1
    return prob_matrix


def conductance(parties, mwc, prob_matrix):
    """
    Function calculates the Conductance of the probability matrix.

    Calculates the internal strength and external pull of the mwc then divides the latter by the sum of both.
    """

    # Internal Strength
    edges = list(it.combinations(mwc, 2))  # Creates all edge pairings of the mwc in the graph
    everything_in = 0
    everything_out = 0
    for edge in edges:
        row = parties.index(edge[0])  # Since prob matrix and parties have the same ordering of the parties...
        column = parties.index(edge[1])  # ...this lines up the rows and columns.
        everything_in += prob_matrix[row][column]

    # External Pull
    for party in mwc:
        row = parties.index(party)
        for i in range(len(parties)):
            if prob_matrix[row][i] != 0 and parties[i] not in mwc:  # Checks if the column currently being looked at
                # is associated with a party not in the mwc and is > 0
                everything_out += prob_matrix[row][i]

    # Final conductance
    psi = (everything_out / (everything_out + (2 * everything_in)))
    return psi


def cep(parties, mwc, prob_matrix):
    """
    Finds the Coalition Existence Probability of each mwc.

    Does this in the same way as internal strength in conductance function but multiplies instead of adds.
    """
    edges = list(it.combinations(mwc, 2))  # Creates all edge pairings of the mwc in the graph
    cep = 1
    for edge in edges:
        row = parties.index(edge[0])  # Since prob matrix and parties have the same ordering of the parties...
        column = parties.index(edge[1])  # ...this lines up the rows and columns.
        cep *= prob_matrix[row][column]  # Multiplies instead of adds
    return cep
