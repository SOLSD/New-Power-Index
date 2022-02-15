import numpy as np


def party_hits_target_check(parties, target):
    for i in range(len(parties)):
        if parties[i][0] >= target:
            return i
    return -1


def winning_party(parties, index):
    final_scores = []
    for i in range(len(parties)):
        name = parties[i][-1]
        if i == index:
            final_scores.append((name, 1))
        else:
            final_scores.append((name, 0))
    return final_scores


def sum_is_target_check(parties, target):
    total = 0
    for i in range(len(parties)):
        total += parties[i][0]
    if total == target:
        return True
    return False


def same_name_check(parties):
    for i in range(len(parties)):
        for j in range(len(parties)):
            if i != j and parties[i][-1] == parties[j][-1]:
                print("Party", i+1, "and Party", j+1, "are the same. Rename them.")
                return True
    return False


def can_reach_target(parties, target):
    total = 0
    for i in range(len(parties)):
        total += parties[i][0]
    if total < target:
        return True
    return False

