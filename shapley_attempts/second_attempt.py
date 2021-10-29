'''
Created on 10 Medi 2021

@author: solsd

Attempt 2 takes Attempt 1 and primarily tries to deal with the issue that Attempt 1 is unable to compute the
correct power indices when multiple parties have equal weightings. Again, there will be little to no attempt
to optimise memory space or running time.
'''

'''
Steps involved in the algorithm:
    1. Determine all sequential coalitions.
    2. Find the pivotal party in each coalition.
    3. Calculate the power index of each party.
'''
import math
import numpy as np
import itertools as it

weightings = [21, 47, 32, 5, 18]
target = 75
listOfPivotalParties = np.zeros(len(weightings))
finalPowerIndices = []
'''
----------------------------------------------------------------------------------------------------------------
Step 1
----------------------------------------------------------------------------------------------------------------
'''


def sequential_coalitions(weightings):
    weightings = list(it.permutations(weightings))  # Generates all permutations of the weightings
    for x in range(len(weightings)):
        vote_accumulation(target, weightings[x])  # Accumulates the votes for each permutation


'''
----------------------------------------------------------------------------------------------------------------
Step 2
----------------------------------------------------------------------------------------------------------------
'''


def vote_accumulation(target, sequential_ordering):

    '''
    TODO:
        Replace .index() method with one that will find all occurrences of argument and return that as a list
        Use that new list to find the index of the argument in the original weightings list
    '''
    accumulation = 0
    for x in range(len(sequential_ordering)):
        party = sequential_ordering[x]
        accumulation = accumulation + party  # Calculates cumulative votes for each ordering
        if accumulation >= target:
            pivotalParty = weightings.index(party)
            listOfPivotalParties[pivotalParty] = listOfPivotalParties[pivotalParty] + 1  # Adds 1 to the number
            # of times that party is pivotal
            break


'''
----------------------------------------------------------------------------------------------------------------
Step 3
----------------------------------------------------------------------------------------------------------------
'''


def calculate_power(listOfPivotalParties):
    n = len(listOfPivotalParties)

    denominator = math.factorial(n)

    '''
    Iterate over list to calculate fraction, then adds fraction to the final list
    '''
    for x in range(len(listOfPivotalParties)):
        numerator = listOfPivotalParties[x]
        finalPowerIndices.append((numerator / denominator))

    return finalPowerIndices


sequential_coalitions(weightings)
print(calculate_power(listOfPivotalParties))