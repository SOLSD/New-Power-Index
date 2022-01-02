import numpy as np


def party_hits_target_check(parties, target):
    for i in range(len(parties)):
        if parties[i][-1] >= target:
            return i
    return -1


def winning_party(parties, index):
    final_scores = []
    for i in range(len(parties)):
        name = parties[i][0]
        if i == index:
            final_scores.append((name, 1))
        else:
            final_scores.append((name, 0))
    return final_scores


def sum_is_target_check(parties, target):
    final_scores = []
    total = 0
    for i in range(len(parties)):
        total += parties[i][-1]
    if total == target:
        return True
    return False

