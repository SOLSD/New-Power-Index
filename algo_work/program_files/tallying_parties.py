tally = []


def tally_up(mwc):
    if len(tally) == 0:  # Makes sure there is an entry to iterate over
        tally.append((mwc[0][-1], 0))
    for i in range(len(mwc)):
        count = 0   # It's a Surprise Tool That Will Helps Us Later
        for j in range(len(tally)):
            if mwc[i][-1] in tally[j][0]:
                tally_count = tally[j][-1]
                tally.pop(j)    # Replaces the tuple
                tally.insert(j, (mwc[i][-1], tally_count + 1))
                break
            else:
                count += 1  # Counting each time the party being checked isn't in the list
                if count >= len(tally):  # If not in list at all (count == length) add to list
                    tally.append((mwc[i][-1], 1))
    return tally


def final_tally(tally):
    final_tally = []
    denominator = 0
    for party in tally:
        denominator += party[-1]    # Denominator is sum of all tallies
    for party in tally:
        tally = party[-1]/denominator
        final_tally.append((party[0], tally))
    return final_tally

