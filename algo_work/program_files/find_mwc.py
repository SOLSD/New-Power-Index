from itertools import combinations


def generate_coalitions(lst, target):
    """
    Finds all combinations needed from parties

    Takes the list of parties and cycles through,
    creating a list of all winning combinations.

    """
    list_of_mwc = []
    index = 0
    for i in range(1, len(lst)+1):
        combination = list(combinations(lst, i))  # Finds all combinations of size i from lst
        # list function coverts into list format, result is a list of all combinations of size i
        for j in range(len(combination)):
            coalition_to_test = list(combination[j])  # Each combination in list is extracted to then be tested
            total = 0
            for k in range(len(coalition_to_test)):
                total += coalition_to_test[k][-1]  # Total is the sum of the votes in each coalition
            if minimal_test(coalition_to_test, total, target):
                list_of_mwc.insert(index, coalition_to_test)
    return list_of_mwc


def minimal_test(combination, total, target):
    """
    Takes combination and checks if it is minimal

    The each party's votes are removed from the total one at a time
    and if for all parties, each time that happens the total is
    smaller than the target, the combination is minimal.
    """
    count = 0
    for i in range(len(combination)):
        check = total - combination[i][-1]
        if check < target:
            count += 1
    if count == len(combination) and total >= target:
        return True
    return False
