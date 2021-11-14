def generate_coalitions(lst, target):
    """
    Finds all combinations needed from parties

    Takes the list of parties and cycles through,
    creating a list of all winning combinations.

    """
    list_of_mwc = []
    index = 0
    for i in range(len(lst)):
        if i != len(lst) - 1:  # Checks if element last in list
            combination = [lst[i]]
            total = lst[i][-1]
            for j in range(len(lst)):
                if i != j and i < j:
                    combination.append(lst[j])
                    total += lst[j][-1]
                    if total >= target and (minimal_test(combination, total, target)):
                        list_of_mwc.insert(index, combination)
                        index += 1
                        break
            continue
    print(list_of_mwc)


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
    if count == len(combination):
        return True
    return False
