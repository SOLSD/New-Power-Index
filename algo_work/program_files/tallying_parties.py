
def tally(mwcs):
    """
    Takes a list of MWCs and counts up how many times a party appears across all of them.
    """

    list_of_lists = [item for t in mwcs for item in t]  # Takes mwcs and converts from a list of list of tuples to a
    # list of tuples
    storage = []
    denominator = len(list_of_lists)
    scores = []

    for i in range(len(list_of_lists)):
        if storage.count(list_of_lists[i]) == 0:  # Checks if the party has already been counted
            storage.append(list_of_lists[i])
            count = list_of_lists.count(list_of_lists[i])
            score_tuple = (list_of_lists[i][0], count/denominator)
            scores.append(score_tuple)
    print(scores)
    return scores

tally([[('A', 2), ('B', 5), ('D', 4), ('F', 8)], [('C', 3), ('D', 4), ('E', 3), ('F', 8)], [('A', 2), ('B', 5), ('C', 3), ('F', 8)]])
