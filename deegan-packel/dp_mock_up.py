import itertools as it
from collections import Counter


class Party:
    def __init__(self, name, votes):
        self.name = name
        self.votes = votes


A = Party("A", 2)
B = Party("B", 5)
C = Party("C", 7)
D = Party("D", 3)
parties = [A, B, C, D]
target = 10


def find_coalitions(list_of_parties):
    lst = []
    list_of_mwcs = []
    for i in range(len(list_of_parties)):
        lst.append(list_of_parties[i].votes)
    for i in range(len(list_of_parties)):
        coalition = list(it.combinations(lst, i + 1))
        for j in range(len(coalition)):
            if test_for_mwc(list(coalition[j])):
                list_of_mwcs.append((list(coalition[j])))
    count_tally(list_of_mwcs, parties)


def test_for_mwc(list_of_coalitions):
    count = 0
    if sum(list_of_coalitions) < target:
        return False
    for i in range(len(list_of_coalitions)):
        value_to_save = list_of_coalitions[i]
        list_of_coalitions.pop(i)
        if sum(list_of_coalitions) < target:
            count += 1
        list_of_coalitions.insert(i, value_to_save)
    if count == len(list_of_coalitions):
        return True
    return False


def count_tally(list_of_mwcs, parties):
    for i in range(len(list_of_mwcs)):
        for j in range(len(list_of_mwcs[i])):
            k = list_of_mwcs[i][j]
            print(k)
            print(list_of_mwcs[i], list_of_mwcs[i][j].count(k))



print(find_coalitions(parties))
