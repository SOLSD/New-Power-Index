from itertools import combinations
import graph_theory_section, all_the_lambda, tallying_parties


def find_min_coalition(parties, target):
    """
    Function to find minimum number of parties needed to make an MWC
    """
    votes = []
    min_start = 0
    for party in parties:
        votes.append(party[0])  # Adds party votes to list
    votes = sorted(votes)  # Puts list in numerical order
    total = 0
    for i in range(len(votes) + 1):
        total += votes[-i]  # Adds party votes together and checks if it's more than target
        if total >= target:
            min_start = i  # If total is more than target then that is min number of parties needed
            break
    return min_start


def generate_coalitions(parties, target, starting_point, prob_matrix):
    """
    Finds all combinations needed from parties

    Takes the list of parties and cycles through,
    creating a list of all winning combinations.

    """

    for i in range(starting_point, len(parties)+1):
        all_combos = combinations(parties, i)  # generates all combinations of length i from parties list
        for combo in all_combos:
            total = 0
            for j in range(len(combo)):
                total += combo[j][0]  # Calculates total votes for each coalition
            if total < target:
                continue
            if minimal_test(combo, total, target):  # Checks if coalition is M and W

                print(combo)

        psi = graph_theory_section.conductance(parties, combo, prob_matrix)  # Finds conductance of MWC
        cep = graph_theory_section.cep(parties, combo, prob_matrix)  # Finds existence probability of MWC
        Lambda = all_the_lambda.assign_Lambda(combo, psi, cep)  # Finds lambda value of MWC
        tally = tallying_parties.tally_up(combo)



def minimal_test(combination, total, target):
    """
    Takes combination and checks if it is minimal

    The each party's votes are removed from the total one at a time
    and if for all parties, each time that happens the total is
    smaller than the target, the combination is minimal.
    """
    count = 0
    for i in range(len(combination)):
        check = total - combination[i][0]  # Removes one party from coalition one at a time to check if minimal
        if check < target:
            count += 1  # Every time the coalitions total falls under the target is counted.
    if count == len(combination) and total >= target:  # If the removal of every party in the coalition results in the
        # rest not reaching the target then the coalition is minimal
        return True
    return False
