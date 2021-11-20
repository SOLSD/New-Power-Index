
def tally(mwcs):
    list_of_lists = [item for t in mwcs for item in t]
    storage = []
    denominator = len(list_of_lists)

    for i in range(len(list_of_lists)):
        if storage.count(list_of_lists[i]) == 0:
            storage.append(list_of_lists[i])
            count = list_of_lists.count(list_of_lists[i])
            get_score(list_of_lists[i][0], count, denominator)


def get_score(party_name, count, denominator):
    print("Score for party ", party_name, " is ", (count/denominator))


tally([[('B', 5), ('C', 3), ('D', 4), ('E', 3)], [('D', 4), ('E', 3), ('F', 8)]])
