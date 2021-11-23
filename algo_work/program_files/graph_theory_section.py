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
                prob_matrix[j][i] = prob  # Makes matrix symmetrical
    return prob_matrix


def conductance(parties, mwcs, prob_matrix):
    """
    Function calculates the Conductance of the probability matrix.

    Calculates the internal strength and external pull of the mwc then divides the latter by the sum of both.
    """
    print(prob_matrix)
    conductances = []
    for mwc in mwcs:

        # Internal Strength
        print("-----------------")
        print("INTERNAL STRENGTH")
        print("-----------------")
        vertices = list(it.combinations(mwc, 2))  # Creates all vertex pairings of the mwc in the graph
        everything_in = 0
        everything_out = 0
        for vertex in vertices:
            row = parties.index(vertex[0])  # Since prob matrix and parties have the same ordering of the parties...
            column = parties.index(vertex[1])  # ...this lines up the rows and columns.
            everything_in += prob_matrix[row][column]
            print("Vertex:", vertex, "; Row:", row, "; Column:", column, "; To add:", prob_matrix[row][column],
                  "; New everything_in:", everything_in)
        print(everything_in)

        # External Pull
        print("-------------")
        print("EXTERNAL PULL")
        print("-------------")
        for party in mwc:
            row = parties.index(party)
            for i in range(len(parties)):
                if prob_matrix[row][i] != 0 and parties[i] not in mwc:  # Checks if the column currently being looked at
                    # is associated with a party not in the mwc and is > 0
                    everything_out += prob_matrix[row][i]
                    print("Added", prob_matrix[row][i], "External pull now", everything_out)
        print(everything_out)

        # Final conductance
        psi = (everything_out / (everything_out + (2 * everything_in)))
        conductances.append((mwc, psi))
    print(conductances)
    return conductances


def cep(parties, mwcs, prob_matrix):
    ceps = []
    for mwc in mwcs:
        vertices = list(it.combinations(mwc, 2))  # Creates all vertex pairings of the mwc in the graph
        cep = 1
        for vertex in vertices:
            row = parties.index(vertex[0])  # Since prob matrix and parties have the same ordering of the parties...
            column = parties.index(vertex[1])  # ...this lines up the rows and columns.
            cep *= prob_matrix[row][column]
        ceps.append((mwc, cep))
    print(ceps)
    return ceps

