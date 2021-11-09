def generate_coalitions(lst, target):
    """
    Finds all combinations needed from parties

    Takes the list of parties and cycles through,
    creating a list of all winning combinations.

    """
    for i in range(len(lst)):
        if i != len(lst) - 1:   # Checks if element last in list
            combination = [lst[i]]
            total = lst[i][-1]
            for j in range(len(lst)):
                if i != j and i < j:
                    combination.append(lst[j])
                    total += lst[j][-1]
                    if total >= target:
                        test_for_mwc(combination, target)


def test_for_mwc(combination, target):
    count = 0
    for party in combination:


