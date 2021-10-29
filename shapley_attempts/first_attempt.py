'''
Created on 8 Medi 2021

@author: solsd

Attempt 1 is a rough attempt at generating Shapley-Shubik power indices with a small number of parties.
There will be no attempt to significantly optimise memory or time.
This implementation will not handle multiple parties of the same weightings well.
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

weightings = [18, 47, 32, 5, 15]
target = 36
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

    accumulation = 0
    for x in range(len(sequential_ordering)):
        party = sequential_ordering[x]
        accumulation = accumulation + party # Calculates cumulative votes for each ordering
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
        finalPowerIndices.append((numerator/denominator))
    
    return finalPowerIndices
            

sequential_coalitions(weightings)
print(calculate_power(listOfPivotalParties))