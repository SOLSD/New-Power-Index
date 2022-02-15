from itertools import combinations
import graph_theory_section, all_the_lambda, tallying_parties


def find_min_coalition(parties, target):
    votes = []
    min_start = 0
    for party in parties:
        votes.append(party[0])
    votes = sorted(votes)
    total = 0
    for i in range(len(votes) + 1):
        total += votes[-i]
        if total >= target:
            min_start = i
            break
    return min_start


def generate_coalitions(parties, target, starting_point, prob_matrix):
    """
    Finds all combinations needed from parties

    Takes the list of parties and cycles through,
    creating a list of all winning combinations.

    """
    num_mwcs = 0
    num_all = 0
    for i in range(starting_point, len(parties)+1):
        all_combos = combinations(parties, i)
        for combo in all_combos:
            total = 0
            num_all += 1
            for j in range(len(combo)):
                total += combo[j][0]
            print("%d / %d" % (num_mwcs, num_all))
            if minimal_test(combo, total, target):
                num_mwcs += 1
                psi = graph_theory_section.conductance(parties, combo, prob_matrix)
                cep = graph_theory_section.cep(parties, combo, prob_matrix)
                Lambda = all_the_lambda.assign_Lambda(combo, psi, cep)
                tally = tallying_parties.tally_up(combo)
            if total < target:
                break
            else:
                continue
    print("%d / %d" % (num_mwcs, num_all))
    print("Percentage of all combinations is: %f" % (num_mwcs/num_all))
    print("Lambda is:", Lambda)
    print("Tally is:", tally)
    return (Lambda, tally)


def minimal_test(combination, total, target):
    """
    Takes combination and checks if it is minimal

    The each party's votes are removed from the total one at a time
    and if for all parties, each time that happens the total is
    smaller than the target, the combination is minimal.
    """
    count = 0
    for i in range(len(combination)):
        check = total - combination[i][0]
        if check < target:
            count += 1
    if count == len(combination) and total >= target:
        return True
    return False
